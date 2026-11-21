"""Rigenera la tabella "quanto costa su importi tipici" di 02-incassi/commissioni.md.

Uso: python calcola_commissioni.py
Aggiornare TARIFFE dalle fonti ufficiali prima di eseguirlo.
"""
TARIFFE = {  # nome: (percentuale, quota fissa €)
    "Stripe carta SEE standard": (1.5, 0.25),
    "Stripe carta SEE premium": (2.8, 0.25),
    "Stripe carta extra-UE": (3.15, 0.25),
    "PayPal con conto": (3.4, 0.35),
    "PayPal carta senza conto": (1.2, 0.35),
    "Satispay (≥ 10 €)": (0.95, 0),
    "SumUp POS": (1.95, 0),
    "Klarna via Stripe (minimo)": (4.99, 0.40),
    "Bonifico": (0, 0),
}
IMPORTI = (12, 18, 25, 45, 100)


def cella(importo: float, perc: float, fisso: float) -> str:
    if perc == 0 and fisso == 0:
        return "0"
    c = importo * perc / 100 + fisso
    return f"{c:.2f} ({c / importo * 100:.1f}%)".replace(".", ",")


if __name__ == "__main__":
    print("| Strumento | " + " | ".join(f"{i} €" for i in IMPORTI) + " |")
    print("|---|" + "---|" * len(IMPORTI))
    for nome, (p, f) in TARIFFE.items():
        print(f"| {nome} | " + " | ".join(cella(a, p, f) for a in IMPORTI) + " |")
