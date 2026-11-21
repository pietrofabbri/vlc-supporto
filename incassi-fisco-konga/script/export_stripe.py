"""Export mensile dei movimenti Stripe per la contabilità.

Uso: python export_stripe.py AAAA-MM
Richiede: pip install stripe · variabile STRIPE_RESTRICTED_KEY (rk_live_..., permessi di sola lettura)
Produce: stripe_AAAA-MM_dettaglio.csv e stripe_AAAA-MM_giornaliero.csv (separatore ;)
"""
import csv
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal

import stripe

stripe.api_key = os.environ["STRIPE_RESTRICTED_KEY"]


def limiti_mese(aaaa_mm: str) -> tuple[int, int]:
    a, m = map(int, aaaa_mm.split("-"))
    inizio = datetime(a, m, 1, tzinfo=timezone.utc)
    fine = datetime(a + (m == 12), m % 12 + 1, 1, tzinfo=timezone.utc)
    return int(inizio.timestamp()), int(fine.timestamp())


def main(aaaa_mm: str) -> None:
    gte, lt = limiti_mese(aaaa_mm)
    righe = []
    giorni = defaultdict(lambda: defaultdict(Decimal))
    for bt in stripe.BalanceTransaction.list(created={"gte": gte, "lt": lt}, limit=100).auto_paging_iter():
        giorno = datetime.fromtimestamp(bt.created, timezone.utc).date().isoformat()
        lordo, comm, netto = (Decimal(x) / 100 for x in (bt.amount, bt.fee, bt.net))
        cat = bt.reporting_category  # charge, refund, dispute, payout, fee, ...
        righe.append([bt.id, giorno, cat, bt.source or "", f"{lordo:.2f}", f"{comm:.2f}", f"{netto:.2f}", bt.currency])
        giorni[(giorno, cat)]["lordo"] += lordo
        giorni[(giorno, cat)]["commissioni"] += comm
        giorni[(giorno, cat)]["netto"] += netto

    with open(f"stripe_{aaaa_mm}_dettaglio.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "giorno", "categoria", "sorgente", "lordo", "commissioni", "netto", "valuta"])
        w.writerows(righe)
    with open(f"stripe_{aaaa_mm}_giornaliero.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["giorno", "categoria", "lordo", "commissioni", "netto"])
        for (g, c), v in sorted(giorni.items()):
            w.writerow([g, c, f"{v['lordo']:.2f}", f"{v['commissioni']:.2f}", f"{v['netto']:.2f}"])
    tot_comm = sum(v["commissioni"] for v in giorni.values())
    print(f"Commissioni totali {aaaa_mm}: {tot_comm:.2f} € (confrontare con il documento commissioni Stripe)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
