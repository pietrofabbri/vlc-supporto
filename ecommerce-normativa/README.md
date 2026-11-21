# E-commerce e normativa

[← vlc-supporto](../README.md)

Documentazione per **Volta la Carta** (Ferrara): vendita online, obblighi di legge in Italia e UE, buone pratiche per sito ed e-commerce, quadro dell'azienda, strumenti di lavoro.

> Informazione, non consulenza legale o fiscale. Le scelte che vincolano vanno confermate con un avvocato, il commercialista o il consulente privacy.

**Aggiornato al:** 21/11/2026 · **Versione:** 1.6.0 · [Changelog](CHANGELOG.md)

## Da dove partire

1. [**Sintesi**](01-sintesi/sintesi.md): cosa è stato fatto, l'azienda in cinque righe, le regole che contano.
2. [**Prossimi passi**](01-sintesi/prossimi-passi.md): checklist operativa in ordine di priorità.
3. [**Quadro e piano**](02-azienda/quadro-e-piano.md): profilo completo, risposte da chiarire, profilo per i bandi.
4. [**Registro di conformità**](04-registro-conformita/registro-conformita.md): 35 obblighi con stato, note, perché e come.
5. [**Calendario delle scadenze**](03-normativa/00-calendario-scadenze.md) e [ultimo monitoraggio](03-normativa/monitoraggio/2026-11.md).

## Priorità di oggi

| # | Azione | Registro |
|---|--------|----------|
| 1 | Banner cookie: oggi assente con Google Analytics e Meta Pixel attivi | o15 |
| 2 | Condizioni di vendita: esclusioni dal recesso (lavori su misura) e chi paga il reso | o02, o09 |
| 3 | Cercare e togliere il link ODR | o34 |
| 4 | Riscrivere o togliere le parole "green" sul sito | o23 |
| 5 | Dati dell'editore/fabbricante nelle schede prodotto | o21 |

## Struttura

```
ecommerce-normativa/
├── README.md                     ← sei qui
├── CHANGELOG.md                  ← storico delle versioni e voci da monitorare
├── 01-sintesi/                   ← sintesi del lavoro e prossimi passi
├── 02-azienda/                   ← profilo, quadro e piano, questionario HTML,
│   └── risposte-questionari/       risposte ai tre questionari in tabella
├── 03-normativa/                 ← calendario scadenze + 10 moduli normativi
│   └── monitoraggio/               report mensili automatici
├── 04-registro-conformita/       ← copia del registro online (35 obblighi)
├── 05-sito-web/                  ← piattaforma, performance, SEO e ricerca AI, UX, sicurezza,
│                                   pagine legali, confronto strumenti
├── 06-commerce/                  ← catalogo, checkout, pagamenti, spedizioni e resi,
│                                   marketplace e commercio agentico, email e CRM
├── 07-gestione-azienda/          ← KPI, customer care, magazzino, AI in azienda,
│                                   governance, strumenti attivi
├── 08-checklist/                 ← conformità legale, lancio sito, revisione trimestrale
├── 09-modelli/                   ← 7 bozze di documenti e procedure (da far revisionare)
├── 10-formazione/                ← quiz sulle regole 2026
├── 11-fonti/                     ← fonti con data di consultazione
├── 12-strumenti/                 ← skill di verifica, monitoraggi automatici, sorgente del registro
└── _template/                    ← modello per nuovi moduli
```

## Moduli normativi

| # | Tema | File |
|---|------|------|
| 01 | Recesso e pulsante di recesso | [01-codice-consumo-recesso.md](03-normativa/01-codice-consumo-recesso.md) |
| 02 | Prezzi, sconti, recensioni | [02-prezzi-promozioni-recensioni.md](03-normativa/02-prezzi-promozioni-recensioni.md) |
| 03 | Privacy, GDPR, cookie | [03-privacy-gdpr-cookie.md](03-normativa/03-privacy-gdpr-cookie.md) |
| 04 | Accessibilità (EAA) | [04-accessibilita-eaa.md](03-normativa/04-accessibilita-eaa.md) |
| 05 | Sicurezza prodotti (GPSR) | [05-sicurezza-prodotti-gpsr.md](03-normativa/05-sicurezza-prodotti-gpsr.md) |
| 06 | Green claims | [06-green-claims-greenwashing.md](03-normativa/06-green-claims-greenwashing.md) |
| 07 | Imballaggi (PPWR) | [07-imballaggi-ppwr.md](03-normativa/07-imballaggi-ppwr.md) |
| 08 | IVA e fiscalità UE | [08-iva-fiscalita-ue.md](03-normativa/08-iva-fiscalita-ue.md) |
| 09 | AI Act | [09-ai-act.md](03-normativa/09-ai-act.md) |
| 10 | Controversie, ADR, fine ODR | [10-controversie-adr.md](03-normativa/10-controversie-adr.md) |

## Convenzioni
- Un tema per file; intestazione con `ultimo_aggiornamento`, `stato` (`attuale` / `da-verificare` / `superato`) e fonti.
- Priorità: 🔴 obbligo di legge · 🟠 fortemente consigliato · 🟢 buona pratica.
- Fonti numerate in [`11-fonti/fonti.md`](11-fonti/fonti.md) (`F..`, `N..`), richiamate nei moduli.
- Ogni modifica va nel [CHANGELOG](CHANGELOG.md). Per un nuovo modulo parti da [`_template/`](_template/template-modulo.md).

## Fonti di verità
- **Registro online** (claude.ai) per lo stato degli obblighi; la copia qui è una fotografia.
- **Progetto "Info legislative"** (claude.ai) per i moduli normativi aggiornati dal monitoraggio mensile.
- Questa cartella raccoglie tutto in un unico posto, versionato. La strategia di sviluppo (valutazione delle idee, studi di mercato, bandi) è in [`../strategia/`](../strategia/README.md); i CSV originali dei tre questionari in [`../strategia/valutazione-idee/risposte/`](../strategia/valutazione-idee/risposte/).
