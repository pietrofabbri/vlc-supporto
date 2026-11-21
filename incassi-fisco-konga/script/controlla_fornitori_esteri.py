"""Controllo mensile delle fatture dei fornitori esteri (per i TD17).

Uso: python controlla_fornitori_esteri.py AAAA-MM [cartella_base]

Si aspetta i PDF in <cartella_base>/AAAA-MM/ con nome "fornitore_AAAA-MM-GG.pdf"
(es. "Fornitori esteri/2026-11/google_2026-11-03.pdf").
"""
import pathlib
import sys

# fornitore: tipo di TD17 — aggiornare quando cambia un abbonamento
ATTESI = {
    "meta": "22%",
    "google": "22%",
    "adobe": "22%",
    "canva": "22%",
    "stripe": "N4",
}


def main(mese: str, base: str = "Fornitori esteri") -> int:
    cartella = pathlib.Path(base) / mese
    file_pdf = sorted(cartella.glob("*.pdf")) if cartella.exists() else []
    conteggio: dict[str, int] = {}
    for p in file_pdf:
        nome = p.name.split("_")[0].lower()
        conteggio[nome] = conteggio.get(nome, 0) + 1

    print(f"Fornitori esteri — {mese}  ({cartella})")
    mancanti = 0
    for fornitore, tipo in ATTESI.items():
        n = conteggio.get(fornitore, 0)
        if n:
            print(f"  ✔ {fornitore:<8} {tipo:<4} {n} fattur{'a' if n == 1 else 'e'} → {n} TD17")
        else:
            print(f"  ✘ {fornitore:<8} {tipo:<4} MANCA")
            mancanti += 1
    extra = sorted(set(conteggio) - set(ATTESI))
    if extra:
        print("  ? Fornitori non previsti (aggiungerli ad ATTESI?):", ", ".join(extra))
    print(f"Totale TD17 da preparare: {sum(conteggio.values())} · scadenza: 15 del mese successivo")
    return 1 if mancanti else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:3]))
