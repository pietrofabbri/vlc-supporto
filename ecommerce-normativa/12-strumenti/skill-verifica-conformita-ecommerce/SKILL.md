---
name: verifica-conformita-ecommerce
description: Controlla schede prodotto, testi promozionali, email, pagine del sito, packaging o claim per la conformità e-commerce B2C in Italia e UE.
---

# Verifica conformità e-commerce (Italia + UE)

Usa questa skill quando l'utente chiede di controllare, rivedere o scrivere un testo o una pagina destinata ai clienti: scheda prodotto, descrizione, annuncio di sconto, newsletter, pagina del sito, condizioni di vendita, testo di confezione o etichetta, post social, risposta di un chatbot.

Rispondi in italiano. Ricorda in una riga, in fondo, che si tratta di verifica informativa e non di consulenza legale.

## 1. Carica il riferimento aggiornato
Se è disponibile il progetto "Info legislative", leggi con lo strumento Projects:
- `claude/ecommerce-calendario-scadenze-normative.md` (per sapere cosa è in vigore oggi)
- il modulo pertinente in `ecommerce/normativa/` (01 recesso, 02 prezzi/recensioni, 03 privacy/cookie, 04 accessibilità, 05 GPSR, 06 green claims, 07 imballaggi, 08 IVA, 09 AI Act, 10 ADR)
- l'ultimo report in `ecommerce/monitoraggio/` se esiste.
Se il progetto non è disponibile, usa le regole qui sotto e segnala che potrebbero non essere aggiornate.

## 2. Controlli per tipo di contenuto

### Scheda prodotto
- Caratteristiche essenziali presenti (materiali, misure, contenuto, compatibilità, formato).
- Prezzo totale IVA inclusa; spese extra indicate prima del checkout.
- GPSR: nome e recapiti (postale ed elettronico) del fabbricante; se extra-UE, persona responsabile UE; elementi identificativi (immagine, tipo, lotto o codice); avvertenze di sicurezza in italiano.
- Claim ambientali: niente termini generici (eco, green, sostenibile, impatto zero, neutro) senza prova specifica; ambito del claim corretto (prodotto vs confezione).
- Durabilità/riparabilità/ricambi/aggiornamenti dove pertinente.
- Immagini con testo alternativo (accessibilità).
- Per libri ed e-book: ISBN, autore, editore, formato, lingua; gli e-book rientrano nell'European Accessibility Act.

### Sconti e promozioni
- Prezzo precedente mostrato = prezzo più basso applicato nei 30 giorni prima della riduzione (art. 17-bis Codice del consumo).
- Nessuna scarsità o countdown falsi; condizioni dell'offerta chiare (durata, prodotti inclusi, limiti).
- Concorsi a premi: verificare regole DPR 430/2001.

### Recensioni
- Indicato se e come si verifica che provengano da acquirenti reali; nessuna recensione falsa o selezione ingannevole.

### Email e newsletter
- Base giuridica (consenso o soft-spam verso clienti per prodotti analoghi); link di disiscrizione; one-click unsubscribe tecnico per invii massivi.

### Pagine del sito e condizioni di vendita
- Dati impresa (P.IVA, REA, sede, PEC).
- Recesso: 14 giorni, eccezioni indicate, modulo tipo, collocazione della funzione/pulsante di recesso online (art. 54-bis, dal 19/06/2026).
- Garanzia legale di conformità 2 anni.
- Nessun link alla piattaforma ODR (chiusa dal 20/07/2025).
- Pulsante d'ordine che indica l'obbligo di pagare.

### Contenuti generati con AI e chatbot
- Chatbot: dichiara di essere un'AI nell'interfaccia (AI Act art. 50, dal 02/08/2026) e offre passaggio a un operatore.
- Immagini o video realistici generati: etichetta visibile se possono sembrare reali.

### Packaging ed etichette
- Claim ambientali come sopra; indicazioni ambientali di smaltimento; ricorda obblighi PPWR (dichiarazione di conformità, EPR) se si parla di nuovi imballaggi.

### Accessibilità (per pagine e componenti)
- Contrasto, struttura dei titoli, etichette dei campi, uso da tastiera, alternative testuali.

## 3. Formato della risposta
1. Una riga di esito: Conforme / Da correggere / Rischio alto.
2. Tabella dei problemi: | Punto | Problema | Norma | Priorità (🔴 obbligo, 🟠 consigliato, 🟢 miglioramento) | Correzione proposta |
3. Testo corretto completo, pronto da incollare, se l'utente ha fornito un testo.
4. Cosa serve sapere o verificare che non si può dedurre dal testo (es. prezzo dei 30 giorni precedenti, certificazioni, dati del fabbricante).

Non inventare certificazioni, dati del fabbricante o prove: se mancano, lasciali come segnaposto [DA COMPLETARE].
