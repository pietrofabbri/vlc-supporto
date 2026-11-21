# Strategia di incasso

> Aggiornato al 16/10/2026 · Basato sul [profilo](../01-profilo/profilo.md)

**Regola:** lo strumento più economico che il cliente accetta in quel contesto, con il **minor numero di fornitori possibile**, perché ogni fornitore estero aggiunge un documento TD17 al mese.

## Quale strumento per cosa

| Situazione | Strumento | Dettagli |
|---|---|---|
| Studente o privato al banco | POS della banca, contanti, **+ Satispay** per gli importi piccoli | [negozio-laboratorio](negozio-laboratorio.md) |
| Università, dipartimenti, enti, musei | Fattura PA → bonifico | [pa-mepa](pa-mepa.md) |
| Aziende, studi professionali, librerie | Fattura elettronica → bonifico con numero fattura in causale | [strumenti § bonifico](strumenti.md#bonifico-sdd-riba) |
| Ordine dal sito | **Stripe** (carte, Apple/Google Pay) + bonifico come alternativa | [strumenti § Stripe](strumenti.md#stripe) |
| Clienti esteri (in futuro) | Stripe; PayPal da valutare solo allora | [oss-estero](../03-fisco/oss-estero.md) |

## Raccomandazione

| Canale | Oggi | Consiglio |
|---|---|---|
| Banco | POS banca + contanti | Tenere il POS, recuperare il contratto per conoscerne il costo, aggiungere Satispay (QR sul bancone) |
| PA | Fattura PA → bonifico | Invariato; curare CIG, codice ufficio, split payment |
| Sito | Stripe + bonifico (preferito dai clienti) | Mettere la carta in primo piano; per il bonifico, causale = numero d'ordine scritta nell'email di conferma |
| Librerie | Fattura → bonifico | Chiedere il numero di fattura in causale; QR di pagamento sul PDF di cortesia |
| PayPal | Non usato | **Non aprirlo per ora** |

## Perché
- Con pochi ordini online, meno strumenti significano meno documenti mensili: è proprio la priorità del titolare.
- Il bonifico è gratuito ma lento da controllare (movimenti non scaricati, causali senza riferimenti); la carta con Stripe si abbina da sola.
- Satispay è italiano: le sue fatture passano dallo SDI e non creano adempimenti esteri (⚠️ da confermare).

## Rispetto alla guida e-commerce
La guida generale [ecommerce-normativa/06-commerce/03-pagamenti.md](../../ecommerce-normativa/06-commerce/03-pagamenti.md) consiglia 4–6 metodi sul sito, PayPal compreso. Per Volta la Carta oggi la scelta è più stretta per due motivi: pochi ordini online al mese e la priorità di ridurre gli adempimenti per i fornitori esteri. Se gli ordini online crescono o si inizia a vendere all'estero, conviene tornare a quella guida e aggiungere PayPal e i wallet.

## Da evitare
- Aprire PayPal, Klarna o altri strumenti esteri "per sicurezza".
- Bonifici senza causale strutturata.
- Considerare le "fatture" di Stripe come fatture fiscali: la fattura la emette solo Konga via SDI.
- Conti di pagamento personali per incassi aziendali; saldi lasciati fermi sugli strumenti di pagamento.
