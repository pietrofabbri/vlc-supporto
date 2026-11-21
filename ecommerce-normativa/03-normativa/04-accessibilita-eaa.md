---
titolo: Accessibilità digitale — European Accessibility Act e Linee guida AgID
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
ambito: [IT, UE]
si_applica_a: [B2C]
fonti: [F01, F02, F03]
---

# Accessibilità (EAA)

## In breve
Dal **28 giugno 2025** gli e-commerce rivolti ai consumatori devono essere accessibili alle persone con disabilità: **D.Lgs. 82/2022**, che recepisce la Dir. (UE) 2019/882. Il **4 marzo 2026** AgID ha adottato le **Linee guida sull'accessibilità dei servizi** e dall'**11 marzo 2026** è attiva una piattaforma dove chiunque può segnalare un servizio non accessibile. Le regole c'erano già; nel 2026 è arrivato il meccanismo per farle rispettare. [F02][F03]

## Chi è obbligato
- Servizi di commercio elettronico verso consumatori: sito, app, flusso d'acquisto, gestione account, pagamenti. [F02]
- Se l'e-commerce è usabile anche dai consumatori, va reso conforme **nella sua interezza**. [F01]
- **Esenzione:** microimprese che forniscono servizi (meno di 10 dipendenti e fatturato o bilancio annuo ≤ 2 M€). L'esenzione non vale per i *prodotti* coperti dall'EAA (es. e-reader). Anche se esente, conviene adeguarsi: riduce attriti e contestazioni. [F01]
- Gli **e-book** sono nell'ambito dell'EAA: rilevante per chi pubblica o vende libri digitali.

## Le aree più critiche per un e-commerce [F01]
1. **Checkout, login e pagamenti** — il cuore del servizio.
2. **Informazioni obbligatorie** (prezzi, condizioni, recesso) leggibili da tecnologie assistive.
3. **Modifiche future**: ogni nuova funzione va verificata, non basta un audit una tantum.

## 🔴 Requisiti tecnici (riferimento: EN 301 549 → WCAG 2.1 AA; puntare a WCAG 2.2 AA)
- Testi alternativi per immagini prodotto informative.
- Navigazione completa **da tastiera**, focus visibile, nessuna trappola (es. pop-up non chiudibili).
- **Contrasto** minimo 4.5:1 per il testo normale.
- Moduli con etichette, errori spiegati in testo (non solo colore), istruzioni chiare.
- Struttura con titoli gerarchici (H1–H3), landmark, lingua della pagina dichiarata.
- Zoom fino al 200% senza perdita di contenuti; layout responsive.
- Video con sottotitoli; nessun contenuto che lampeggia.
- Target touch abbastanza grandi (WCAG 2.2: almeno 24×24 px).
- CAPTCHA con alternativa accessibile.
- **Dichiarazione di accessibilità** pubblicata: come il servizio soddisfa i requisiti e come segnalare problemi (il modello AgID per la PA può essere adattato). 

## 🟠 Fortemente consigliato
- Audit iniziale con test automatici (axe, WAVE, Lighthouse) **più** test manuali con lettore di schermo (NVDA, VoiceOver).
- Inserire l'accessibilità nei criteri di accettazione di ogni sviluppo ("accessibility by design").
- Evitare gli overlay "magici" che promettono conformità con uno script: non risolvono i problemi di fondo.
- Canale per segnalazioni di accessibilità con risposta entro tempi definiti.

## Sanzioni
AgID vigila sui servizi: può ordinare misure correttive, il ritiro del servizio non conforme e gestisce i reclami degli utenti. Verifica gli importi aggiornati nel D.Lgs. 82/2022.

## Come verificare (15 minuti)
1. Scollega il mouse e completa un acquisto.
2. Attiva VoiceOver/NVDA e ascolta la scheda prodotto: si capisce prezzo e variante?
3. Esegui Lighthouse → sezione Accessibility ≥ 90 come soglia minima (non sufficiente da sola).

## Collegamenti
- [04-ux-design-mobile.md](../05-sito-web/04-ux-design-mobile.md)
- [01-codice-consumo-recesso.md](01-codice-consumo-recesso.md) (anche il pulsante di recesso deve essere accessibile)
