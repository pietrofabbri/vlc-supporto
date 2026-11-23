# Osservatorio dei componenti

[← Monitoraggio](README.md)

Registro cumulativo di patch, aggiornamenti, vulnerabilità e accortezze di sicurezza sui componenti di **tutti i siti** di Volta la carta. Lo alimenta ogni lunedì l'attività pianificata *Sicurezza sito rilegaretesi*.

- **Ogni settimana**: le novità si aggiungono in cima al [Registro](#registro), senza notifica.
- **Ogni mese** (primo lunedì): [confronto mensile](#confronti-mensili) tra il registro e i componenti in uso, con notifica.
- **Subito** se emerge qualcosa di grave: vulnerabilità sfruttata attivamente, critica senza autenticazione, o un attacco alla supply chain che tocca un nostro componente.

Fonti primarie: advisory del progetto, GitHub Security Advisories, OSV, NVD, CISA KEV, blog di sicurezza dei fornitori (Wordfence, Patchstack per i plugin WordPress). Una notizia vista solo su fonti secondarie si segna come *da verificare*.

## Componenti seguiti

| Sito | Componente | Versione in uso | Dove si legge |
| --- | --- | --- | --- |
| rilegaretesi.it attuale | WordPress core | Da rilevare | Bacheca WordPress |
| rilegaretesi.it attuale | WooCommerce | Da rilevare | Bacheca WordPress |
| rilegaretesi.it attuale | Elementor (ed Elementor Pro, se presente) | Da rilevare | Bacheca WordPress |
| rilegaretesi.it attuale | Altri plugin e tema, PHP dell'hosting | Da rilevare | Bacheca WordPress, pannello hosting |
| voltalacarta.it | WordPress core, plugin, tema, PHP | Da rilevare | Bacheca WordPress |
| rilegaretesi.it nuovo (`rt2`) | pdf.js (incluso in `src/assets/vendor/pdfjs`) | 4.10.38 | `pdf.mjs` |
| rilegaretesi.it nuovo (`rt2`) | Font `@fontsource` installati con `npm i` nel workflow | Non fissata | `.github/workflows/pages.yml` riga 33 |
| rilegaretesi.it nuovo (`rt2`) | GitHub Actions (checkout, setup-node, setup-python, pages, markdownlint, lychee) | Per tag, non SHA | `.github/workflows/` |
| rilegaretesi.it nuovo (previsto) | Cloudflare Workers, wrangler, R2, D1, Access, Turnstile | Non ancora usati | `docs/architettura-produzione.md` |
| rilegaretesi.it nuovo (previsto) | Stripe Checkout e SDK, Resend | Non ancora usati | `docs/architettura-produzione.md` |
| App del second brain | Token GitHub fine-grained, GitHub Pages | — | Decisione 0008 |
| Tutti | npm (ecosistema), GitHub Actions (ecosistema) | — | Campagne di supply chain |

Quando una versione "da rilevare" viene letta, va scritta qui con la data.

## Registro

Dal più recente. Impatto: 🔴 ci tocca e va agito subito · 🟠 ci tocca, da pianificare · 🟢 non ci tocca oggi, da ricordare · ❔ da verificare se ci tocca.

| Data | Componente | Novità | Versione corretta | Impatto per noi | Fonte |
| --- | --- | --- | --- | --- | --- |
| 18/11/2026 | WordPress core | Release di sicurezza con 20 correzioni; la più grave è un'escalation di privilegi **senza autenticazione** tramite gli attributi del blocco Template Part, che può portare a esecuzione di codice | 7.1.5 (rami precedenti: 7.0.9, 6.9.12 … 4.7.40) | 🔴 rilegaretesi.it attuale e voltalacarta.it: verificare la versione e aggiornare | [WordPress 7.0.9](https://wordpress.org/documentation/wordpress-version/version-7-0-9/) |
| 03/11/2026 | WordPress core | CVE-2026-119977: race condition nell'aggiornamento che espone per poco l'installer; CVSS 8.1, **sfruttata attivamente** (inserita nel catalogo CISA KEV) | 7.1.4 (e rami 7.0.8, 6.9.11, 6.8.12 …) | 🔴 superata da 7.1.5: basta aggiornare all'ultima. *Da verificare* su fonte primaria (CISA KEV) | [Tech Insider](https://tech-insider.org/wordpress-cve-2026-119977-cisa-kev-7-1-4-deadline-nov-6-2026/) |
| 08/2026 | Elementor Pro | Caricamento di file arbitrari **senza autenticazione** tramite il campo upload dei moduli | > 4.2.1 | ❔ Solo se sui siti WordPress c'è Elementor Pro con moduli di upload. *Da verificare*: pagina Wordfence non leggibile da qui | [Wordfence](https://www.wordfence.com/blog/2026/08/critical-arbitrary-file-upload-vulnerability-patched-in-elementor-pro-wordpress-plugin/) |
| 2026 | WooCommerce | SQL injection per utenti autenticati con ruolo Shop Manager o superiore | > 10.9.4 | ❔ Rischio basso se nessuno ha quel ruolo oltre ai titolari; aggiornare comunque. *Da verificare* | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/woocommerce/woocommerce-1094-authenticated-shop-manager-sql-injection) |
| 06/08/2026 | pdf.js (`pdfjs-dist`) | CVE-2026-16633 (GHSA-hq66-cqwq-w95j): un PDF malevolo può eseguire JavaScript nel dominio che lo mostra, con `enableScripting` attivo e senza CSP; CVSS 4.0 8.6 | 6.2.108 | 🟢 `rt2` usa 4.10.38, fuori dall'intervallo colpito (5.6.83 – 6.2.107). Se si aggiorna pdf.js, andare almeno a 6.2.108; tenere `enableScripting: false` e una CSP | [OSV](https://osv.dev/vulnerability/CVE-2026-16633) |
| 04/08/2026 | npm (ecosistema) | Worm *ChainDrop*, variante di Shai-Hulud: oltre 400 pacchetti compromessi, script `preinstall` che ruba credenziali di sviluppo e CI e ripubblica pacchetti | — | 🟠 `rt2/.github/workflows/pages.yml` riga 33 fa `npm i` senza versioni fissate né `--ignore-scripts` (già segnalato il 21/11) | [Microsoft Security](https://microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm) |
| 20/01/2026 | wrangler (Cloudflare) | CVE-2026-0933: command injection in `wrangler pages deploy` tramite `--commit-hash`; CVSS 4.0 7.7 | 3.114.17 / 4.59.1 | 🟢 Non ancora usato. Quando arriva il Worker: wrangler ≥ 4.59.1 | [OSV](https://osv.dev/vulnerability/CVE-2026-0933) |

## Confronti mensili

Ogni primo lunedì del mese: per ogni voce del registro non ancora chiusa, si confronta la versione corretta con quella in uso e si indica cosa resta da fare.

### Dicembre 2026

Primo confronto previsto per lunedì 07/12/2026.
