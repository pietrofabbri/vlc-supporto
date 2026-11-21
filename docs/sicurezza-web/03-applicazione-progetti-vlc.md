# Sicurezza web applicata ai progetti di Volta la carta

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

Applicazione dei [profili di progetto](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/16-progetti/profili-di-progetto.md) ai progetti decisi in [0008](https://github.com/voltalacarta/documentazione/blob/main/10-decisioni/0008-app-web-del-second-brain-su-github-pages.md) e [0009](https://github.com/voltalacarta/documentazione/blob/main/10-decisioni/0009-rifare-i-siti-rilegaretesi-it-e-voltalacarta-it-per-vendere.md) e descritti nel [piano digitale](https://github.com/voltalacarta/documentazione/blob/main/50-progetti/piano-digitale.md).

> Stato **bozza**: è una proposta di lettura dei rischi, non una decisione. Va confermata quando si scelgono le tecnologie.

## Quadro

| Progetto | Profilo | Moduli | ASVS | Urgenza |
| --- | --- | --- | --- | --- |
| **rilegaretesi.it attuale** (WordPress + WooCommerce) | C · E-commerce | UGC | L2 | 🔴 Subito: vende oggi |
| **rilegaretesi.it nuovo** (`voltalacarta/rt2`, staging su GitHub Pages) | C · E-commerce | UGC, API | L2 | 🔴 Prima del lancio di metà gennaio 2027 |
| **voltalacarta.it** (restyling) | A · Vetrina, C se vende online | — | L1 / L2 | 🟠 Con il restyling |
| **App del second brain** (GitHub Pages + token GitHub) | B · Area con credenziali | API | L2 | 🟠 Già in uso |

## rilegaretesi.it attuale: finché resta online

È il sito che incassa oggi, quindi ha la priorità più alta finché non viene sostituito.

- 🔴 Core, WooCommerce, Elementor e plugin **aggiornati**, con aggiornamenti automatici di sicurezza.
- 🔴 **Rimuovere** plugin e temi inutilizzati.
- 🔴 MFA su tutti gli account amministratore; un account per persona.
- 🔴 Backup automatico fuori dal server, con un ripristino provato.
- 🟠 Header e blocchi di base: [`apache.htaccess`](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/13-ricettario/apache.htaccess) e [hardening WordPress](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/13-ricettario/wordpress-hardening.md).
- 🟠 Verifica rapida con `check-headers.py` (vedi [strumenti](04-strumenti-e-modelli.md)).
- 🔴 **Cookie**: sul sito WooCommerce attuale Google Analytics e Meta Pixel sono attivi senza banner di consenso (voce o15 del [registro di conformità](../../ecommerce-normativa/04-registro-conformita/registro-conformita.md)). Va sistemato subito, oppure si tolgono i tracker.

## rilegaretesi.it nuovo: punti di attenzione

Flusso previsto: il cliente configura, **carica il PDF**, paga (carta, Apple/Google Pay, PayPal); l'ordine finisce nel Registro VLC (Google Sheets) e il file su Drive.

| Punto | Rischio | Controllo consigliato |
| --- | --- | --- |
| **Hosting statico su GitHub Pages** | GitHub Pages non permette header HTTP personalizzati: niente CSP via header, niente `frame-ancestors` | CSP via `<meta>` come minimo; per il dominio di produzione valutare un hosting che gestisce gli header (es. Cloudflare Pages o Netlify con `_headers`) |
| **Pagamenti** | Dati di carta | Solo pagine di pagamento **ospitate dal PSP** (es. Stripe Checkout): la carta non passa mai dal sito. Verifica della firma dei webhook |
| **Caricamento del PDF** | File malevoli, file enormi, file di altri clienti esposti | Serve un piccolo backend o una funzione serverless: tipo verificato sui byte, limite di dimensione, nome casuale, storage privato, link firmati a scadenza |
| **Ordini su Google Sheets e Drive** | Credenziali Google esposte nel codice statico | Le credenziali stanno **solo** nella funzione serverless, mai nel sito o nel repository. Account di servizio con accesso alle sole cartelle necessarie |
| **Limite di ordini al giorno** | Abuso del flusso (OWASP API6): prenotazioni fittizie | Limite applicato lato server, non solo nel configuratore; rate limit e anti-bot leggero |
| **Dati personali** | Nome, email, ateneo, contenuto della tesi, dati per la fattura | Informativa privacy, DPA con Stripe, PayPal, Google e Brevo, **cancellazione dei PDF** dopo un periodo definito, consenso marketing separato (già previsto) |
| **Statistiche** | Cookie e consenso | Strumento senza cookie (già previsto: Plausible o Umami) |
| **Repository** | Segreti nei commit | Secret scanning, `.gitignore` di sicurezza, nessuna chiave nel codice |
| **Dominio** | Furto del dominio, email false | MFA e blocco del trasferimento sul registrar; SPF, DKIM, DMARC |

Prima del lancio: [checklist pre-lancio](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/checklist/pre-lancio.md), almeno nelle voci 🔴.

## voltalacarta.it

- 🔴 Togliere le **pagine di prova pubbliche** e i duplicati segnalati nell'analisi del 13/10/2026: oltre al danno SEO aumentano la superficie esposta.
- 🔴 Stesse regole WordPress di rilegaretesi.it finché resta su WordPress.
- 🟠 Se il restyling porta a un sito statico, il rischio scende molto (profilo A).

## App del second brain (decisione 0008)

L'app è statica, in una repo pubblica, e usa un **token personale GitHub** nel browser per leggere e scrivere il second brain privato. La CSP rigida è già prevista.

- 🔴 Token **fine-grained**, limitato alla sola repo `second-brain`, con permessi minimi e **scadenza breve**.
- 🔴 Se il token esce (dispositivo perso, estensione malevola): revocarlo subito da GitHub.
- 🟠 Trusted Types attivi: ora funzionano su tutti i browser.
- 🟠 Nessuno script di terze parti; eventuali librerie con SRI.

## Normativa

| Norma | Applicabile? | Perché |
| --- | --- | --- |
| **GDPR** | ✅ Sì | Dati di clienti e PDF delle tesi |
| **NIS2** | Probabilmente no | Attività e dimensioni non sembrano rientrare nei settori e nelle soglie. Va confermato una volta: se fosse soggetta, la scadenza del 31/10/2026 è già passata |
| **Cyber Resilience Act** | No | Si vendono servizi, non prodotti software |
| **Fatturazione elettronica** | ✅ Sì | Riguarda la gestione dei dati (P.IVA, codice destinatario), non la sicurezza del sito |

## Da usare nei contratti

Se una parte del lavoro va a un'agenzia o a un freelance: [requisiti per capitolati](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/16-progetti/requisiti-capitolato.md) e [questionario fornitori](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/15-modelli/questionario-fornitori.md), dopo revisione legale.
