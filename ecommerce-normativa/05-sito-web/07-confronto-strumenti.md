---
titolo: Confronto strumenti — piattaforme, testi legali e cookie, pagamenti, spedizioni
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-01-15   # i listini cambiano spesso
stato: da-verificare
fonti: [F38, F39, F40, F41, F42, F43]
---

# Confronto strumenti

> Prezzi letti dai listini ufficiali il 15/10/2026, **IVA esclusa** salvo diversa indicazione. Verifica sempre il listino prima di firmare: le condizioni cambiano spesso e possono dipendere da volumi e contratto.

## 1. Piattaforme e-commerce

### Shopify (SaaS)
La pagina prezzi consultata mostrava i prezzi in dollari USA; il listino in euro per l'Italia va verificato su it.shopify.com al momento dell'iscrizione. [F38][F39]

| Piano | Canone mensile (fatturazione mensile / annuale) | Carte online con Shopify Payments | Commissione se usi un altro gateway |
|-------|----------------------------------------------|-----------------------------------|-------------------------------------|
| Basic | 39 $ / 29 $ | 2,9% + 0,30 $ (tariffa USA) | 2% |
| Grow | 105 $ / 89 $ | 2,7% + 0,30 $ | 1% |
| Advanced | 399 $ / 359 $ | 2,5% + 0,30 $ | 0,6% |
| Plus | da 2.300 $ | 2,25% + 0,30 $ | 0,2% |

⚠️ La commissione aggiuntiva per gateway esterni (PayPal, Satispay, Stripe…) si somma a quella del gateway stesso. Le tariffe Shopify Payments in Italia sono diverse da quelle USA: controllale nel pannello. Una fonte terza riporta per Grow 79 $/mese con fatturazione annuale: altro motivo per verificare. [F39]

### WooCommerce e PrestaShop (open source)
Software gratuito, ma i costi reali sono: hosting adeguato (da qualche decina a qualche centinaio di € al mese per negozi con traffico), tema, estensioni a pagamento (abbonamenti, spedizioni, fatturazione elettronica, B2B), manutenzione e aggiornamenti di sicurezza, sviluppatore. Nessuna commissione della piattaforma sul venduto.

### Come scegliere
| Se… | Orientati verso |
|-----|-----------------|
| Vuoi partire in fretta, senza team tecnico | SaaS (Shopify o simili) |
| Hai già un sito WordPress con molti contenuti (es. blog, catalogo editoriale) | WooCommerce |
| Catalogo grande, molte varianti, esigenze B2B | PrestaShop / Magento o SaaS di fascia alta |
| Vuoi visibilità sulle superfici AI senza sviluppo | SaaS con canali AI già integrati (vedi [commercio agentico](../06-commerce/05-marketplace-e-commerce-agentico.md)) |

Calcola il **costo totale a 3 anni** su un fatturato realistico: canone + commissioni % sul venduto + app + sviluppo.

## 2. Testi legali e gestione cookie (iubenda)

| Piano | Mensile | Annuale (al mese) | Banner cookie / CMP | Privacy policy | Termini e condizioni | Visualizzazioni incluse |
|-------|---------|-------------------|---------------------|----------------|----------------------|-------------------------|
| Essentials | 5,99 € | 4,99 € | ✅ | ✅ | ❌ | 25.000/mese |
| Advanced | 21,99 € | 19,99 € | ✅ | ✅ | ✅ | 50.000/mese |
| Ultimate | 89,99 € | 79,99 € | ✅ | ✅ | ✅ | 150.000/mese |

Prezzi per sito, IVA esclusa. [F40]
- Oltre il limite di visualizzazioni: 0,05 € ogni 1.000. La pagina dà indicazioni contrastanti su cosa succede al banner oltre il limite: chiedilo a iubenda prima di scegliere il piano. [F40]
- Le prove del consenso per moduli e newsletter costano a parte: 5 €/mese ogni 1.000 consensi oltre il primo blocco. [F40]
- Esistono componenti aggiuntivi per l'accessibilità (non inclusi nel confronto).
- Per un e-commerce servono i **Termini e condizioni** → minimo piano Advanced, oppure testi scritti da un legale.

Alternative da valutare con lo stesso schema: altre CMP certificate Google (es. Cookiebot, Cookie Script), testi legali dell'avvocato + CMP separata.

## 3. Pagamenti

| Metodo | Commissione standard | Note |
|--------|----------------------|------|
| **Stripe** – carte SEE standard | 1,5% + 0,25 € | [F41] |
| Stripe – carte SEE premium | 2,8% + 0,25 € | [F41] |
| Stripe – carte UK | 2,5% + 0,25 € (+2% se conversione valuta) | [F41] |
| Stripe – carte internazionali | 3,15% + 0,25 € (+2% se conversione) | [F41] |
| Stripe – Klarna | da 4,99% + 0,40 € | [F41] |
| Stripe – addebito SEPA | 0,35 € | [F41] |
| **PayPal** Checkout (Italia e SEE) | 3,40% + 0,35 € | mittenti UK +1,29%, altri Paesi +1,99% [F42] |
| PayPal – pagamenti con carta (Advanced) | 1,20% + 0,35 € (piano misto) | Amex 3,50% [F42] |
| **Satispay** | 0% sotto 10 €, 0,95% da 10 € in su | nessun canone fisso; tabella generale riportata per i negozi, verificare le condizioni e-commerce [F43] |

**Lettura pratica**
- Su un ordine da 40 € con carta SEE standard: Stripe ≈ 0,85 €; PayPal ≈ 1,71 €; Satispay ≈ 0,38 €.
- Offrire PayPal costa di più, ma molti clienti italiani lo preferiscono: valuta il tasso di conversione, non solo la commissione.
- Su Shopify con gateway esterni aggiungi la commissione della piattaforma (vedi sopra).

## 4. Software di spedizione

Prezzi **da verificare** (non è stato possibile leggere i listini in questa revisione). Criteri di confronto:

| Criterio | Domanda |
|----------|---------|
| Corrieri integrati | Poste/SDA, BRT, GLS, DHL, UPS, InPost/locker? Tariffe pre-negoziate o contratti propri? |
| Integrazioni | Con la tua piattaforma e i marketplace |
| Portale resi | Si collega alla funzione di recesso obbligatoria? |
| Tracking brandizzato | Email e pagina di tracking con il tuo marchio |
| Costi | Canone + costo per etichetta + eventuali soglie |

Strumenti diffusi in Italia: ShippyPro, Sendcloud, Packlink, oltre alle app dei singoli corrieri.

## Come aggiornare questo modulo
Una volta l'anno (o prima di rinnovare un contratto) rileggi i listini ufficiali, aggiorna le tabelle e le fonti F38–F43.
