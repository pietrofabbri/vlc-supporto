---
titolo: Sintesi del lavoro (ottobre–novembre 2026)
ultimo_aggiornamento: 2026-11-21
---

# Sintesi del lavoro

Schema di tutto quello che è stato prodotto nelle conversazioni con Claude del 15–16 ottobre 2026, con gli aggiornamenti di novembre.

## 1. Cosa è stato fatto

| # | Passo | Risultato | Dove |
|---|-------|-----------|------|
| 1 | Ricerca di best practice per siti web, e-commerce e gestione, e della normativa IT/UE aggiornata a ottobre 2026 | Guida modulare in file .md | Cartelle 03, 05–08, 11 |
| 2 | Modelli di documenti | 7 bozze: condizioni di vendita, informativa privacy, dichiarazione di accessibilità, policy AI, procedure data breach, richiamo prodotto, reclami | [`09-modelli/`](../09-modelli/README.md) |
| 3 | Confronto strumenti | Listini di piattaforme, gestori cookie, pagamenti | [`05-sito-web/07-confronto-strumenti.md`](../05-sito-web/07-confronto-strumenti.md) |
| 4 | Registro di conformità online | 35 obblighi con stato, note, "perché e come" | Pagina su claude.ai; copia in [`04-registro-conformita/`](../04-registro-conformita/registro-conformita.md) |
| 5 | Monitoraggio normativo mensile automatico | Primo report il 1/11/2026 | [`03-normativa/monitoraggio/`](../03-normativa/monitoraggio/2026-11.md) |
| 6 | Formazione | Quiz di 10 domande sulle regole 2026 | [`10-formazione/`](../10-formazione/quiz-regole-2026.md) |
| 7 | Skill di verifica | Controllo automatico di testi e pagine | [`12-strumenti/skill-verifica-conformita-ecommerce/`](../12-strumenti/skill-verifica-conformita-ecommerce/SKILL.md) |
| 8 | Questionario per il titolare | File HTML da email, 77 domande chiuse (anche bandi), esporta CSV | [`02-azienda/questionario-azienda.html`](../02-azienda/questionario-azienda.html) |
| 9 | Analisi delle risposte (tre questionari) | Profilo, incongruenze, piano di lavoro, profilo per i bandi | [`02-azienda/quadro-e-piano.md`](../02-azienda/quadro-e-piano.md) |

## 2. L'azienda in cinque righe
- **Volta la Carta**, Ferrara: ditta individuale in contabilità ordinaria, 1–2 persone, fatturato sotto 100.000 € → **microimpresa**.
- Casa editrice (oltre 100 titoli, 11–20 novità l'anno, tutti con ISBN) + stampa e rilegatura (500–1.500 tesi l'anno) + cartoleria.
- Clienti soprattutto aziende ed enti; abilitata al **MePA**.
- Sito **WooCommerce** con pochi ordini (0–50 al mese), solo Italia; incassi Stripe, POS, bonifico; gestionale **Konga**.
- Nessun debito, plafond de minimis pieno, DURC regolare, PEC e firma digitale.

Dettaglio: [`02-azienda/profilo.md`](../02-azienda/profilo.md).

## 3. Le regole che contano (stato a novembre 2026)

| Regola | In vigore dal | Riguarda Volta la Carta? |
|--------|---------------|--------------------------|
| Pulsante di recesso online (D.Lgs. 209/2025) | 19/06/2026 | ✅ Sì — presente, da verificare il flusso |
| Green claims (D.Lgs. 30/2026) | 27/09/2026 | ✅ Sì — parole "green" sul sito da sistemare |
| Cookie e privacy (GDPR, Garante 2021) | in vigore | ✅ Sì — **manca il banner** con Analytics e Pixel attivi |
| Sicurezza prodotti (GPSR) | 13/12/2024 | ✅ Sì — dati dell'editore/fabbricante nelle schede |
| Link ODR da togliere | 20/07/2025 | ✅ Da controllare |
| Imballaggi (PPWR) | 12/08/2026 | ❓ Da verificare con il commercialista (riuso imballaggi, CONAI) |
| Accessibilità (EAA) | 28/06/2025 | ⚪ Esente come microimpresa (consigliata) |
| AI Act art. 50 | 02/08/2026 | ⚪ No — nessuno strumento AI |
| IVA OSS / ViDA | 2021 / 01/01/2027 | ⚪ No — nessuna vendita UE |
| Credito ai consumatori (BNPL) | 20/11/2026 | ⚪ No — nessun pagamento rateale ai privati |
| Digital Omnibus cookie, Digital Fairness Act | non prima del 2027 | Da seguire |

Calendario completo: [`03-normativa/00-calendario-scadenze.md`](../03-normativa/00-calendario-scadenze.md).

## 4. Decisioni prese lungo il lavoro
- Documentazione in **file .md modulari**, uno per tema, con data e stato in testa e un CHANGELOG.
- Questionario come **file HTML da mandare via email** (niente account, niente installazioni), con export CSV; tolte le domande su chi segue il sito, tempo settimanale e priorità; aggiunte domande su editoria, vendite, sicurezza e bandi; box note facoltativo a fine sezione.
- Registro di conformità **online** come versione di lavoro; le copie .md sono fotografie.
- Monitoraggio normativo **mensile** automatico che aggiorna il progetto "Info legislative".
