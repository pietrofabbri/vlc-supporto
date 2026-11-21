"""Trasforma stripe_AAAA-MM_giornaliero.csv in righe di prima nota da importare a mano in Konga.

Uso: python prepara_prima_nota.py stripe_2026-11_giornaliero.csv
Riferimento per un eventuale passo futuro: oggi le registrazioni si fanno a mano.
I nomi dei conti e il tracciato di import vanno allineati a Konga (chiedere a EasyByte).
"""
import csv
import sys

CONTO_PSP = "Stripe c/transitorio"
CONTO_RICAVI = "Corrispettivi vendite online"
CONTO_BANCA = "Banca c/c"
CONTO_COMMISSIONI = "Commissioni su incassi elettronici"
CONTO_SOSPESI = "Sospesi da classificare"


def main(percorso: str) -> None:
    with open(percorso, encoding="utf-8-sig") as f, open("prima_nota_da_importare.csv", "w", newline="", encoding="utf-8-sig") as out:
        w = csv.writer(out, delimiter=";")
        w.writerow(["data", "rif_esterno", "conto_dare", "conto_avere", "importo", "descrizione"])
        for r in csv.DictReader(f, delimiter=";"):
            g, cat = r["giorno"], r["categoria"]
            lordo, comm = float(r["lordo"]), float(r["commissioni"])
            rif = f"stripe:{g}:{cat}"
            if cat == "charge":
                w.writerow([g, rif, CONTO_PSP, CONTO_RICAVI, f"{lordo:.2f}", "Vendite Stripe"])
            elif cat == "refund":
                w.writerow([g, rif, CONTO_RICAVI, CONTO_PSP, f"{-lordo:.2f}", "Rimborsi Stripe"])
            elif cat == "payout":
                w.writerow([g, rif, CONTO_BANCA, CONTO_PSP, f"{-lordo:.2f}", "Payout Stripe"])
            elif lordo:
                # commissioni autonome, contestazioni, rettifiche: mai ignorarle, altrimenti il saldo non torna
                dare, avere = (CONTO_SOSPESI, CONTO_PSP) if lordo < 0 else (CONTO_PSP, CONTO_SOSPESI)
                w.writerow([g, rif, dare, avere, f"{abs(lordo):.2f}", f"Stripe {cat} da verificare"])
            if comm:
                w.writerow([g, rif + ":fee", CONTO_COMMISSIONI, CONTO_PSP, f"{comm:.2f}", "Commissioni Stripe"])
    print("Creato prima_nota_da_importare.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
