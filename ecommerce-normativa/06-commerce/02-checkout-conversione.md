---
titolo: Checkout e ottimizzazione della conversione
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F32, F33]
---

# Checkout e conversione

## I numeri di riferimento (Baymard Institute)
- Tasso medio documentato di abbandono del carrello: circa **70%** (media di 50 studi). [F33]
- Il checkout medio ha 23,48 elementi di modulo e 14,88 campi; uno ottimizzato può funzionare con **12–14 elementi, cioè 7–8 campi**. [F33]
- Un grande e-commerce può ottenere in media un **+35% di conversione** solo migliorando il design del checkout. [F32]
- Molti abbandoni sono inevitabili (chi "sta solo guardando"); tra chi aveva intenzione d'acquisto, le cause principali sono costi extra inattesi, obbligo di creare un account, checkout lungo o complicato, dubbi su sicurezza, consegne lente, politiche di reso poco chiare. [F32][F33]
- Nota: i sondaggi Baymard sono su consumatori statunitensi; usali come direzione, poi misura i tuoi dati. [F33]

## 🟠 Checklist checkout
**Costi e trasparenza**
- [ ] Spese di spedizione stimate visibili in scheda prodotto o carrello (per CAP/Paese).
- [ ] Nessun costo aggiunto all'ultimo passo.
- [ ] Data di consegna stimata, non solo "3-5 giorni lavorativi".

**Attrito**
- [ ] **Acquisto come ospite** sempre possibile; proposta di account *dopo* l'ordine.
- [ ] 7–8 campi totali: unire nome/cognome dove possibile, un solo campo indirizzo con autocompletamento, niente "conferma email" ridondante.
- [ ] Indirizzo di fatturazione = spedizione preselezionato.
- [ ] Tastiera giusta su mobile (numerica per CAP e telefono), autocompletamento del browser attivo.
- [ ] Campo Codice fiscale / P.IVA / codice SdI / PEC **solo se** il cliente chiede la fattura.
- [ ] Validazione in tempo reale con messaggi d'errore chiari e accessibili.
- [ ] Riepilogo ordine sempre visibile e modificabile.

**Fiducia e pagamento**
- [ ] Metodi di pagamento preferiti dagli italiani (vedi [03-pagamenti.md](03-pagamenti.md)), wallet in alto su mobile.
- [ ] Loghi pagamento e informazioni sui resi vicino al pulsante finale.
- [ ] Pulsante finale con dicitura conforme che indichi l'obbligo di pagare (es. "Ordina con obbligo di pagamento" / "Acquista ora") — art. 51 Cod. consumo.

**Dopo l'ordine**
- [ ] Pagina di conferma con numero ordine, riepilogo e tempi.
- [ ] Email di conferma immediata (con condizioni di vendita e link alla funzione di recesso).

## Recupero carrelli
- Email di carrello abbandonato solo con consenso o base giuridica valida (vedi [03-privacy](../03-normativa/03-privacy-gdpr-cookie.md)); sequenza tipica: 1 h, 24 h, 72 h.
- Prima si sistemano gli attriti, poi si investe nel recupero: costa meno e ha più effetto.

## Misurare il funnel
Sessione → vista prodotto → aggiunta al carrello → inizio checkout → pagamento → ordine. Analizza separatamente mobile/desktop e per sorgente di traffico; fai **test A/B** su una modifica alla volta.
