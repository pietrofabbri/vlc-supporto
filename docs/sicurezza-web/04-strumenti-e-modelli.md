# Strumenti e modelli pronti per la sicurezza web

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

Tutto sta in [`documentazione/25-sicurezza-web/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web). Qui c'è la mappa.

## Script

| Script | Cosa fa | Come si usa | Verificato |
| --- | --- | --- | --- |
| [`check-headers.py`](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/14-automazione/scripts/check-headers.py) | Controlla header, cookie, TLS, redirect HTTPS, `security.txt`, file esposti (`.git`, `.env`, backup) | `python3 check-headers.py https://sito.it` (aggiungi `--json` per la CI) | ✅ Su server di prova buono e vulnerabile |
| [`kb-revisioni.py`](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/14-automazione/scripts/kb-revisioni.py) | Elenca i file della base da rivedere e i punti incerti | `python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --giorni 30` | ✅ |

`check-headers.py` usa solo la libreria standard di Python. Va usato solo su siti propri o con autorizzazione.

## Automazioni attive

| Dove | Cosa | Quando |
| --- | --- | --- |
| `documentazione` · [`revisioni-sicurezza-web.yml`](https://github.com/voltalacarta/documentazione/blob/main/.github/workflows/revisioni-sicurezza-web.yml) | Apre una issue se ci sono file scaduti o in scadenza | Il 1° di ogni mese (prima issue attesa il 1° dicembre 2026) |
| `documentazione` · `controlli.yml` | markdownlint e lychee | A ogni push |

## Configurazioni pronte (ricettario)

| Stack | File | Verifica |
| --- | --- | --- |
| Apache / hosting condiviso | `apache.htaccess` | Da provare con `apachectl configtest` |
| WordPress | `wordpress-hardening.md` | — |
| nginx | `nginx-security.conf` | Da provare con `nginx -t` |
| Caddy | `caddyfile` → rinominare `Caddyfile` | Da provare con `caddy validate` |
| Netlify | `netlify-headers` → rinominare `_headers` | — |
| Vercel | `vercel.json` | ✅ JSON valido |
| Express | `express-security.js` | ✅ Sintassi |
| Next.js 16 | `nextjs-proxy.ts` | ✅ Allineato alla guida ufficiale |
| Django 6 | `django-settings-security.py` | ✅ Sintassi e documentazione ufficiale |
| Laravel | `laravel-security-headers.php` → rinominare `SecurityHeaders.php` | ✅ Sintassi |

Percorso: [`25-sicurezza-web/13-ricettario/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web/13-ricettario).

## File da copiare in un nuovo progetto

| File | Cosa fa |
| --- | --- |
| `github/workflows/security.yml` | Pipeline: Gitleaks, OSV-Scanner, firme npm, zizmor, header su staging, ZAP mensile. **Fissare le action per SHA** prima dell'uso |
| `github/dependabot.yml` / `renovate.json` | Aggiornamenti con cooldown (usarne uno solo) |
| `config/npmrc` | Script di installazione disattivati, versioni esatte |
| `config/pre-commit-config.yaml` | Blocca i segreti prima del commit |
| `config/gitignore-sicurezza` | Righe da aggiungere al `.gitignore` |

Percorso: [`25-sicurezza-web/14-automazione/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web/14-automazione).

## Documenti da compilare

| Modello | Uso | Revisione legale |
| --- | --- | --- |
| `security.txt` | Contatto per chi trova vulnerabilità | No |
| `politica-divulgazione.md` | Pagina pubblica sulle segnalazioni | ✅ Sì |
| `piano-risposta-incidenti.md` | Ruoli, contatti, termini 24/72 h, runbook | ✅ Sì |
| `registro-violazioni.csv` | Registro GDPR delle violazioni | ✅ Sì |
| `registro-asset-e-accessi.csv` | Chi ha accesso a cosa | No |
| `questionario-fornitori.md` | Domande A1-F2 per agenzie, hosting, SaaS | No |
| `procedura-accessi.md` | Ingresso e uscita di persone e collaboratori | No |
| `requisiti-capitolato.md` | Clausole di sicurezza per i contratti | ✅ Sì |

Percorso: [`25-sicurezza-web/15-modelli/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web/15-modelli) e [`16-progetti/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web/16-progetti).

## Formazione

- [Dieci regole per chi lavora sul sito](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/17-formazione/regole-per-redattori.md): una pagina, da far leggere a ogni collaboratore.
- [Quiz](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/17-formazione/quiz.md): 6 domande per tutti, 9 tecniche.
