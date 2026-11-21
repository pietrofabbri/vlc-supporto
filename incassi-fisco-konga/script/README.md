# Script

Script Python di supporto. Leggono soltanto: nessuno scrive in Konga o modifica gli account.

| Script | Cosa fa | Uso | Richiede |
|---|---|---|---|
| [controlla_fornitori_esteri.py](controlla_fornitori_esteri.py) | ⭐ Elenca le fatture dei fornitori esteri presenti e mancanti nel mese | `python controlla_fornitori_esteri.py 2026-11` | Solo Python |
| [export_stripe.py](export_stripe.py) | Movimenti Stripe del mese: dettaglio e riepilogo giornaliero, totale commissioni | `python export_stripe.py 2026-11` | `pip install stripe`, chiave ristretta in `STRIPE_RESTRICTED_KEY` |
| [calcola_commissioni.py](calcola_commissioni.py) | Rigenera la tabella "quanto costa su importi tipici" | `python calcola_commissioni.py` | Solo Python |
| [export_paypal.py](export_paypal.py) | Transazioni PayPal del mese (se un giorno si apre PayPal) | `python export_paypal.py 2026-11` | `pip install requests`, `PAYPAL_CLIENT_ID`, `PAYPAL_SECRET` |
| [stripe_webhook.py](stripe_webhook.py) | Riceve avvisi da Stripe con verifica della firma (facoltativo) | Servizio HTTPS | `pip install stripe flask`, `STRIPE_WEBHOOK_SECRET` |
| [prepara_prima_nota.py](prepara_prima_nota.py) | Trasforma il riepilogo Stripe in righe di prima nota da importare a mano (riferimento) | `python prepara_prima_nota.py stripe_2026-11_giornaliero.csv` | Solo Python |

## Regole
- Le chiavi stanno in variabili d'ambiente, **mai** nel codice né su GitHub.
- Stripe: usare una **chiave ristretta in sola lettura** (`rk_live_…`).
- I CSV prodotti usano il punto e virgola: si aprono direttamente in Excel.
- I CSV con dati reali **non vanno caricati** in questo repository (vedi `.gitignore`).
