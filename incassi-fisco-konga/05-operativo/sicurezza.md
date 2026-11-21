# Sicurezza

> Verificato il 15/10/2026 · Fonti: [Stripe – chiavi API](https://docs.stripe.com/keys) · [Stripe – webhook](https://docs.stripe.com/webhooks)
> Situazione: verifica in due passaggi solo su alcuni account, qualche password condivisa.

## Account
- [ ] ⭐ **Verifica in due passaggi** su banca, Stripe, email, Google/Meta, Adobe, Canva, intermediario SDI.
- [ ] ⭐ **Niente password condivise**: gestore di password, un accesso per persona (il collaboratore con il suo).
- [ ] Email di recupero degli account = casella aziendale protetta.
- [ ] Accessi a Stripe e banca: solo il titolare (scelta del titolare); il commercialista eventualmente in sola lettura.
- [ ] Revisione degli accessi ogni 6 mesi.

## Chiavi e script
- [ ] Stripe: **chiave ristretta** (`rk_live_…`) solo in lettura per i report; mai la chiave segreta completa negli script.
- [ ] Segreti nel gestore di credenziali di Windows o in variabili d'ambiente, mai nel codice o in file condivisi.
- [ ] Rotazione annuale e subito se un PC si perde o una persona lascia.
- [ ] Sviluppo in modalità test (Stripe test mode).

## Konga
- [ ] ✅ Backup automatico fuori sede; prova di ripristino ogni trimestre.
- [ ] Se un giorno si scrive in Konga da script: utente dedicato, backup prima di ogni import, tutto in transazione.

## Dati e pagamenti
- [ ] Nessun dato di carta nei vostri sistemi: solo pagine di pagamento ospitate (PCI DSS SAQ A).
- [ ] Nei report solo il minimo: numero d'ordine, importi, data, niente indirizzi.
- [ ] Informativa privacy del sito aggiornata con gli strumenti di pagamento usati.

## Truffe
- [ ] Email "da Stripe, PayPal o banca" che chiedono login o cambio IBAN: entrare sempre digitando l'indirizzo.
- [ ] Cambio IBAN di un fornitore: verifica telefonica a un numero già noto.
- [ ] Spedire solo a pagamento confermato.
