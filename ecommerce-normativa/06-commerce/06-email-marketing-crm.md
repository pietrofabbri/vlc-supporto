---
titolo: Email marketing, CRM e fidelizzazione
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F35, F36, N03]
---

# Email marketing e CRM

## 🔴 Requisiti tecnici dei provider (Gmail, Yahoo, Microsoft)
Valgono per chi invia **5.000+ email al giorno** verso caselle personali, ma conviene rispettarli sempre: [F35][F36]
- Autenticazione **SPF, DKIM e DMARC** sul dominio di invio; il dominio del mittente (From) deve essere allineato con SPF o DKIM.
- **Disiscrizione con un clic** (intestazione List-Unsubscribe-Post secondo RFC 8058) sulle email promozionali, con opt-out eseguito entro 2 giorni.
- **Tasso di spam** sotto lo 0,3%, idealmente sotto lo 0,1%; monitoralo con Google Postmaster Tools.
- Microsoft rifiuta del tutto i messaggi che non rispettano i requisiti. [F36]

## 🔴 Requisiti legali (GDPR e Codice privacy)
- Consenso specifico, libero, documentato per newsletter (double opt-in consigliato).
- **Soft-spam** (art. 130 c. 4 Codice privacy): puoi scrivere ai clienti che hanno acquistato, per prodotti analoghi, se hai informato al momento dell'acquisto e offri opt-out in ogni messaggio.
- Profilazione (segmentazione su comportamento di acquisto e navigazione): base giuridica e informativa adeguate.
- Link di disiscrizione in ogni email.

## 🟠 Automazioni che rendono di più
| Flusso | Quando | Obiettivo |
|--------|--------|-----------|
| Benvenuto | Iscrizione | presentare brand e prodotti di punta |
| Carrello abbandonato | 1h / 24h / 72h | recuperare l'ordine |
| Post-acquisto | Spedizione + consegna | rassicurare, istruzioni d'uso |
| Richiesta recensione | 7–14 gg dopo consegna | prova sociale |
| Riacquisto / riassortimento | in base al ciclo di consumo | secondo ordine |
| Riattivazione | 90–180 gg di inattività | recuperare o pulire la lista |
| Torna disponibile | prodotto rientrato | conversione immediata |

## 🟠 CRM e fidelizzazione
- Segmentazione **RFM** (recenza, frequenza, valore) per differenziare messaggi e offerte.
- Programma fedeltà semplice (punti o vantaggi), comunicato con chiarezza (regole del Codice del consumo e, per i concorsi a premi, DPR 430/2001).
- Unificare dati di sito, negozio e marketplace (dove consentito) in un unico profilo cliente.
- Pulizia lista semestrale: gli indirizzi inattivi peggiorano la deliverability.

## KPI
Tasso di apertura (indicativo, falsato dalla privacy di Apple Mail), clic, conversione, ricavi per email inviata, disiscrizioni, tasso di spam.
