# Vendite a università ed enti pubblici (PA e MePA)

> Aggiornato al 15/10/2026 · Fonti: [PartitaIVA.it – split payment prorogato al 30/06/2029](https://www.partitaiva.it/split-payment-proroga/) · [Fiscomania – split payment](https://fiscomania.com/split-payment-proroga/)

Università ed enti sono i **clienti principali del laboratorio**. Volta la Carta è abilitata al **MePA** e ha PEC, firma digitale e DURC regolare. Si incassa **solo con fattura elettronica PA → bonifico**.

## Cosa serve in ogni fattura PA

| Elemento | Cosa | Dove in Konga |
|---|---|---|
| **Codice univoco ufficio** | 6 caratteri, lo comunica l'ente (o indicepa.gov.it) | Anagrafica cliente |
| **CIG** | Obbligatorio per la tracciabilità, lo fornisce l'ente | Dati del documento |
| **Split payment** | L'ente versa l'IVA all'Erario: si incassa **solo l'imponibile**. In vigore fino al **30/06/2029** | Codice IVA / esigibilità "S" |
| Riferimento d'ordine | Numero d'ordine MePA o determina, se richiesto | Riferimenti del documento |
| Conto dedicato | Dichiarazione di tracciabilità con l'IBAN | Una volta per ente |

## Effetti pratici
- In banca arriva **l'imponibile, non il totale**: abbinare il bonifico all'imponibile.
- Righe di **libri** (IVA assolta dall'editore): niente IVA, quindi niente split payment; ❓ dicitura, natura e bollo da 2 € → [domanda 15](../03-fisco/domande-commercialista.md).
- **Tempi**: di norma 30 giorni dalla fattura accettata (60 per alcuni enti, come le aziende sanitarie). I ritardi si vedono nella Piattaforma dei crediti commerciali.
- **Rifiuto**: l'ente può rifiutare la fattura entro 15 giorni (es. CIG mancante, codice ufficio sbagliato) → ❓ nota di credito e nuova fattura: [domanda 16](../03-fisco/domande-commercialista.md).
- L'elenco dei soggetti in split payment esce entro il **20 ottobre** di ogni anno.

## Report utili (solo lettura)
- Settimanale: fatture PA con stato SDI (consegnata, accettata, rifiutata, decorrenza termini).
- Mensile: scadenze a 30 giorni e bonifici arrivati, confrontati con l'imponibile.
