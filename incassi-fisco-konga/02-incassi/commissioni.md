# Commissioni a confronto

> Verificato il 15/10/2026 · **Riverificare ogni 6 mesi** · Unica fonte dei numeri: gli altri file rimandano qui.
> Fonti: [Stripe – tariffe](https://stripe.com/it/pricing) · [PayPal – tariffe dal 15/07/2026 (PDF)](https://www.paypalobjects.com/marketing/ua/pdf/IT/it/it-it-merchant-fees-15-jul-2026.pdf) · [PayPal – tariffe business](https://www.paypal.com/it/business/fees) · [SumUp – costo POS](https://www.sumup.com/it-it/costo-pos/) · [AziendaBanca su Satispay, 24/06/2026](https://www.aziendabanca.it/notizie/tecno/satispay-commissioni-zero-pagamenti-sotto-10-euro)

Tariffe standard di listino; con volumi alti si negoziano. Le commissioni dei servizi di pagamento sono in genere esenti IVA.

## Tariffe

| Strumento | Tariffa | Note |
|---|---|---|
| **Stripe** carte standard SEE | 1,5% + 0,25 € | La maggior parte delle carte italiane |
| Stripe carte premium SEE | 2,8% + 0,25 € | Carte business, alcune premium |
| Stripe carte UK | 2,5% + 0,25 € | |
| Stripe carte internazionali | 3,15% + 0,25 € | +2% con conversione di valuta |
| Stripe Klarna | da 4,99% + 0,40 € | |
| Stripe addebito SEPA | 0,35 € | |
| Stripe Invoicing / Billing / Tax | +0,4% / +0,7% / 0,5% | Invoicing non è fattura elettronica |
| Stripe contestazione | 20 € (+20 € se ci si oppone, rimborsati se si vince) | |
| Stripe payout | Gratis (istantaneo: 1%, min 0,50 €) | |
| **PayPal** con conto PayPal | 3,40% + 0,35 € | Anche "Paga in 3 rate" |
| PayPal carta senza conto | 1,20% + 0,35 € | |
| PayPal QR ≥ 10,01 € / ≤ 10 € | 0,50% + 0,20 € / 2,00% + 0,05 € | ⚠️ tabella ufficiale ambigua |
| PayPal estero | SEE 0 · UK +1,29% · resto del mondo +1,99% | Conversione valuta +3% |
| PayPal contestazione / chargeback | 14 € / 16 € | Sui rimborsi la commissione non torna |
| PayPal POS / Tap to Pay | 1,79% | |
| **Satispay** | 0,95% sopra i 10 €, **0 sotto i 10 €** | ⚠️ confermare sul contratto |
| **SumUp** POS e Tap to Pay | 1,95% | Lettori 34–169 €; con canone (≈16–19 €/mese) 0,95% solo su carte consumer italiane |
| **Bonifico** SEPA / istantaneo | 0 € in entrata (dipende dalla banca) | L'istantaneo non può costare più dell'ordinario (Reg. UE 2024/886) |
| **POS della banca** | ❓ | Recuperare il contratto: canone + % per circuito |

## Quanto costa su importi tipici

Commissione in € (e in % sull'incasso). Calcolata con [script/calcola_commissioni.py](../script/calcola_commissioni.py).

| Strumento | 12 € | 18 € | 25 € | 45 € | 100 € |
|---|---|---|---|---|---|
| Stripe carta SEE standard | 0,43 (3,6%) | 0,52 (2,9%) | 0,62 (2,5%) | 0,93 (2,1%) | 1,75 (1,8%) |
| Stripe carta SEE premium | 0,59 (4,9%) | 0,75 (4,2%) | 0,95 (3,8%) | 1,51 (3,4%) | 3,05 (3,0%) |
| Stripe carta extra-UE | 0,63 (5,2%) | 0,82 (4,5%) | 1,04 (4,2%) | 1,67 (3,7%) | 3,40 (3,4%) |
| PayPal con conto | 0,76 (6,3%) | 0,96 (5,3%) | 1,20 (4,8%) | 1,88 (4,2%) | 3,75 (3,8%) |
| PayPal carta senza conto | 0,49 (4,1%) | 0,57 (3,1%) | 0,65 (2,6%) | 0,89 (2,0%) | 1,55 (1,5%) |
| Satispay (≥ 10 €) | 0,11 (0,9%) | 0,17 (0,9%) | 0,24 (0,9%) | 0,43 (0,9%) | 0,95 (0,9%) |
| SumUp POS | 0,23 (1,9%) | 0,35 (2,0%) | 0,49 (1,9%) | 0,88 (1,9%) | 1,95 (1,9%) |
| Klarna via Stripe (minimo) | 1,00 (8,3%) | 1,30 (7,2%) | 1,65 (6,6%) | 2,65 (5,9%) | 5,39 (5,4%) |
| Bonifico | 0 | 0 | 0 | 0 | 0 |

## Cosa se ne ricava
- Sotto i 20 € pesa soprattutto la **quota fissa** (0,25–0,35 €): spedizione gratuita sopra una soglia e cofanetti alzano lo scontrino medio.
- PayPal costa circa il **doppio** di Stripe sulle carte europee.
- Per copie e stampe al banco, Satispay sotto i 10 € è **gratuito**.
- Klarna ha senso solo per oggetti sopra i 100 €.
