"""Export mensile delle transazioni PayPal (da usare solo se si apre PayPal).

Uso: python export_paypal.py AAAA-MM
Richiede: pip install requests · variabili PAYPAL_CLIENT_ID e PAYPAL_SECRET (app REST con solo Transaction Search)
Note: commissioni con segno negativo; codici evento T00xx pagamenti, T11xx rimborsi, T04xx trasferimenti.
"""
import calendar
import csv
import os
import sys

import requests

BASE = "https://api-m.paypal.com"  # sandbox: https://api-m.sandbox.paypal.com


def token() -> str:
    r = requests.post(
        f"{BASE}/v1/oauth2/token",
        auth=(os.environ["PAYPAL_CLIENT_ID"], os.environ["PAYPAL_SECRET"]),
        data={"grant_type": "client_credentials"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def main(aaaa_mm: str) -> None:
    a, m = map(int, aaaa_mm.split("-"))
    ultimo = calendar.monthrange(a, m)[1]  # massimo 31 giorni per chiamata
    params = {
        "start_date": f"{aaaa_mm}-01T00:00:00+0000",
        "end_date": f"{aaaa_mm}-{ultimo:02d}T23:59:59+0000",
        "fields": "transaction_info",
        "page_size": 500,
        "page": 1,
    }
    h = {"Authorization": f"Bearer {token()}"}
    righe = []
    while True:
        r = requests.get(f"{BASE}/v1/reporting/transactions", headers=h, params=params, timeout=60)
        r.raise_for_status()
        dati = r.json()
        for t in dati.get("transaction_details", []):
            ti = t["transaction_info"]
            lordo = float(ti["transaction_amount"]["value"])
            comm = float(ti.get("fee_amount", {}).get("value", 0))
            righe.append([
                ti["transaction_id"], ti["transaction_initiation_date"][:10], ti["transaction_event_code"],
                ti.get("invoice_id", ""), f"{lordo:.2f}", f"{comm:.2f}", f"{lordo + comm:.2f}",
                ti["transaction_amount"]["currency_code"],
            ])
        if params["page"] >= dati.get("total_pages", 1):
            break
        params["page"] += 1
    with open(f"paypal_{aaaa_mm}.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "giorno", "codice_evento", "rif_ordine", "lordo", "commissioni", "netto", "valuta"])
        w.writerows(righe)
    print(f"{len(righe)} transazioni, commissioni {sum(float(x[5]) for x in righe):.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
