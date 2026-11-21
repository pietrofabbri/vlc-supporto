# Schede degli strumenti di incasso

> Verificato il 15/10/2026 · Commissioni in [commissioni.md](commissioni.md)

## Stripe
**Stato:** ✅ aperto da poco, usato sul sito · Società: Stripe Payments Europe Ltd (Irlanda)

| | |
|---|---|
| Perché | Commissioni basse sulle carte europee, nessun canone, API e report contabili (Balance, Payout reconciliation) in CSV |
| Prodotti utili | Checkout sul sito (nessun dato carta passa da voi) · Payment Links (anche in QR) · Tap to Pay · Billing per abbonamenti |
| Flusso del denaro | Il cliente paga → saldo Stripe al netto della commissione → **payout** periodico in banca (un bonifico per molte vendite) |
| Configurazione | 2FA per tutti · conto e IBAN aziendali · descrittore chiaro (es. `VOLTALACARTA`) · payout settimanali o mensili · numero d'ordine nei metadati · chiave API **ristretta in sola lettura** per i report · Radar attivo |
| Fisco | Documento mensile delle commissioni (esente) → TD17 natura N4: [fornitori esteri](../03-fisco/fornitori-esteri-td17.md) |
| Attenzione | Stripe Invoicing **non** è fattura elettronica · l'account può essere sospeso per verifiche: tenere i documenti pronti · Satispay dentro Stripe è disponibile solo per alcuni esercenti (⚠️ verificare in dashboard) |

## PayPal
**Stato:** ❌ non usato · **Consiglio:** non aprirlo finché non si vende all'estero

| | |
|---|---|
| Pro | Fiducia degli acquirenti meno digitali |
| Contro | 3,40% + 0,35 € · commissione persa sui rimborsi · blocchi di fondi sui conti nuovi · un fornitore estero in più (Lussemburgo) |
| Se un giorno si apre | Conto **Business** aziendale · 2FA · trasferimento automatico in banca · incassare in EUR · app REST con solo *Transaction Search* per i report |

## Satispay
**Stato:** ❌ non usato · **Consiglio:** ✅ aggiungerlo al banco

| | |
|---|---|
| Costo | 0,95% sopra i 10 €, 0 sotto i 10 € (⚠️ cambi frequenti negli ultimi anni) |
| Uso | QR sul bancone; plugin per WooCommerce |
| Pro | Il più economico dopo il bonifico; diffuso tra gli studenti; italiano (niente TD17, ⚠️ da confermare) |
| Contro | Solo clienti con l'app · se usato al banco, ⚠️ verificare se va associato al registratore |

## POS (SumUp, POS bancario, Stripe Terminal)

| Opzione | Costo | Quando |
|---|---|---|
| POS della banca (attuale) | ❓ recuperare il contratto | Già associato al registratore |
| SumUp | 1,95%, nessun canone | Se il POS bancario ha un canone alto rispetto agli incassi |
| Stripe Tap to Pay / Terminal | Tariffe Stripe | Per avere tutto in un account |
| PayPal POS | 1,79% | Non consigliato (PayPal non usato) |

Ogni nuovo POS va **associato al registratore** nell'area *Fatture e Corrispettivi* dell'Agenzia (obbligo dal 1/1/2026).

## Bonifico, SDD, RiBa
**Bonifico** — il canale gratuito per enti, aziende, librerie e parte del sito.
- L'istantaneo costa come l'ordinario; la verifica del beneficiario riduce gli errori di IBAN.
- Chiedere sempre la causale `FT numero/anno` (o il numero d'ordine sul sito).
- QR di pagamento EPC sul PDF di cortesia della fattura (⚠️ letto da molte app bancarie, non da tutte).

**SDD** (addebito diretto) — per abbonamenti o clienti ricorrenti; via Stripe 0,35 € a incasso.

**RiBa** — tipica con clienti commerciali italiani; Konga (modulo Vendite) prepara le distinte.

## Altri canali (non usati oggi)
Distributore, marketplace, e-book, crowdfunding, pagamento a rate: non applicabili. Se diventassero rilevanti: il distributore richiede rendiconti e un metodo IVA preciso; marketplace e piattaforme sono fornitori esteri (TD17); il crowdfunding pone il problema di quando nasce il ricavo.
