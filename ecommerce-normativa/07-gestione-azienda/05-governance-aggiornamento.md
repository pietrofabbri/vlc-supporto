---
titolo: Governance e aggiornamento di questa guida
ultimo_aggiornamento: 2026-10-15
stato: attuale
---

# Governance e aggiornamento

## Ruoli
| Ruolo | Chi | Responsabilità |
|-------|-----|----------------|
| Proprietario della guida | | approva le modifiche, revisione trimestrale |
| Referente legale/privacy | (interno o consulente) | moduli 03-normativa |
| Referente tecnico/web | | moduli 05-sito-web |
| Referente commerciale | | moduli 03 e 04 |

## Ciclo di revisione
- **Trimestrale** (gennaio, aprile, luglio, ottobre): eseguire [`08-checklist/checklist-revisione-trimestrale.md`](../08-checklist/checklist-revisione-trimestrale.md).
- **Straordinaria** quando: nuova legge pubblicata, nuovo canale di vendita, nuovo Paese, superamento soglie (OSS, microimpresa), incidente (data breach, richiamo).

## Come aggiornare un modulo
1. Copia il modulo o parti dal [`_template/template-modulo.md`](../_template/template-modulo.md).
2. Aggiorna `ultimo_aggiornamento`, `prossima_revisione`, `stato`.
3. Aggiungi le fonti nuove in [`11-fonti/fonti.md`](../11-fonti/fonti.md) con nuovo ID e data di consultazione.
4. Se cambia una scadenza, aggiorna anche [`03-normativa/00-calendario-scadenze.md`](../03-normativa/00-calendario-scadenze.md).
5. Annota in [`CHANGELOG.md`](../CHANGELOG.md).

## Dove tenere la guida
- In una cartella condivisa o in un repository Git: ogni modifica resta tracciata.
- Gli editor Markdown (Obsidian, VS Code, Typora) mostrano i collegamenti tra file.
- I file `.md` si convertono facilmente in PDF o Word per condividerli.

## Fonti da monitorare
- Gazzetta Ufficiale / Normattiva — nuove norme italiane
- EUR-Lex — regolamenti e direttive UE
- AGCM (pratiche commerciali), Garante privacy (newsletter), AgID (accessibilità), MIMIT (circolari)
- Netcomm, Osservatori Digital Innovation PoliMi — dati di mercato
- Google Search Central blog — SEO e Core Web Vitals
- Centro Europeo Consumatori Italia — novità per i consumatori
