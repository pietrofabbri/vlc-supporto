# Fattura elettronica e SDI

> Verificato il 15/10/2026 · Fonti: [Blog Konga – fatturazione elettronica](https://blog.konga.it/2018/12/12/konga-versione-1-6-0-fatturazione-elettronica/) · [Manuale contabilità Konga](https://public.easybyte.it/docs/current/contabilita/manuale_contabilita.html)

| Cliente | Regola |
|---|---|
| Aziende, librerie, studi (Italia) | Sempre XML via SDI |
| PA, università statali | Fattura PA con codice ufficio e CIG, split payment → [pa-mepa](../02-incassi/pa-mepa.md) |
| Privati | Solo se richiesta (codice destinatario `0000000`); altrimenti corrispettivi |
| Clienti esteri | Codice destinatario `XXXXXXX` |

## Fatture passive
Arrivano dall'intermediario in Konga (stato `Ricevuto`); dopo la registrazione IVA passano in conservazione.
Utile aggiungere:
- **Pre-imputazione** per fornitore ricorrente (tipografia, corriere, carte).
- **Controllo dell'IBAN** in fattura: se cambia → verifica telefonica a un numero già noto (truffa tipica).
- L'**autorizzazione dei pagamenti** resta sempre umana.

## Conservazione
Obbligo per 10 anni. Volta la Carta: ✅ con il servizio di Konga. Valutare anche il servizio gratuito dell'Agenzia (adesione in *Fatture e Corrispettivi*).

## ❓ Da verificare
- Indirizzo di ricezione SDI (codice destinatario o PEC) registrato sul sito dell'Agenzia → [domanda 18](domande-commercialista.md)
- Dicitura e natura per le righe di libri → [domanda 2](domande-commercialista.md)
