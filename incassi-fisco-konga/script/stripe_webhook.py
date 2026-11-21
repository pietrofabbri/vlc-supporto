"""Ricevitore di avvisi Stripe con verifica della firma (facoltativo).

Serve solo per avvisi immediati (contestazioni, rimborsi, pagamenti falliti). Non tocca Konga:
scrive gli eventi in un file che altri script possono leggere.
Richiede: pip install stripe flask · variabile STRIPE_WEBHOOK_SECRET (whsec_...)
Esporre solo in HTTPS. Test locale: stripe listen --forward-to localhost:5000/webhook/stripe
"""
import json
import os
import pathlib

import stripe
from flask import Flask, abort, request

app = Flask(__name__)
SIGNING_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]
QUEUE = pathlib.Path(os.environ.get("QUEUE_FILE", "eventi_stripe.jsonl"))
SEEN = pathlib.Path(os.environ.get("SEEN_FILE", "eventi_visti.txt"))
EVENTI_UTILI = {
    "charge.dispute.created",
    "charge.refunded",
    "payment_intent.payment_failed",
    "payout.failed",
    "payout.paid",
}


@app.post("/webhook/stripe")
def webhook():
    payload = request.get_data()
    firma = request.headers.get("Stripe-Signature", "")
    try:
        # verifica la firma e rifiuta eventi vecchi (tolleranza 300 s)
        event = stripe.Webhook.construct_event(payload, firma, SIGNING_SECRET)
    except (ValueError, stripe.error.SignatureVerificationError):
        abort(400)

    visti = set(SEEN.read_text().split()) if SEEN.exists() else set()
    if event["id"] in visti:  # nessun duplicato
        return "", 200

    if event["type"] in EVENTI_UTILI:
        rec = {
            "id": event["id"],
            "type": event["type"],
            "object_id": event["data"]["object"]["id"],
            "created": event["created"],
        }
        with QUEUE.open("a") as f:
            f.write(json.dumps(rec) + "\n")
    with SEEN.open("a") as f:
        f.write(event["id"] + "\n")
    return "", 200
