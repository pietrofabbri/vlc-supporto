# Cronologia del lavoro sulla sicurezza web

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

| Data | Versione | Cosa | Risultato |
| --- | --- | --- | --- |
| 2026-10-15 | — | Ricerca sulle best practice 2026 | Sintesi in 9 punti: OWASP Top 10:2025, passkey e NIST, supply chain dopo Shai-Hulud, header, AI, processo, normativa UE |
| 2026-10-15 | 1.0.0 | Knowledge base modulare | 47 file Markdown in 13 aree, con revisione per file, fonti centralizzate e checklist |
| 2026-10-15 | 1.1.0 | Materiale riusabile senza un progetto definito | Ricettario (10 stack), script di controllo, pipeline CI, modelli di documenti, profili di progetto, clausole per i capitolati, formazione. 80 file |
| 2026-10-15 | 1.2.0 | Verifica dei 15 punti incerti sulle fonti primarie | 2 errori corretti (Go post-quantum, Next.js 16); 9 aggiornamenti; resto confermato |
| 2026-10-15 | — | Copia nel progetto Claude "Info tecniche" | 79 file. **Ora superata** dalla versione su GitHub |
| 2026-10-16 | 1.3.0 | Pubblicazione in `voltalacarta/documentazione` come `25-sicurezza-web/` | Adattata alle convenzioni; decisione 0006 proposta; controllo mensile delle revisioni |
| 2026-10-16 | — | Correzione dopo il primo push | Il link di esempio `https://[DOMINIO]/…` faceva fallire lychee; controlli verdi al secondo commit |
| 2026-11-21 | — | Schemi in `vlc-supporto` | Questo repository |

## Commit di riferimento

| Repository | Commit | Contenuto |
| --- | --- | --- |
| `voltalacarta/documentazione` | `f25c5d9` | Sezione `25-sicurezza-web` |
| `voltalacarta/documentazione` | `3ade9f2` | Correzione del link segnaposto |

## Correzioni emerse dalla verifica (1.2.0)

| Argomento | Prima | Dopo la verifica |
| --- | --- | --- |
| Go e post-quantum | Gruppo ibrido disattivato di default | **Attivo di default** da Go 1.24 (sorgente ufficiale) |
| Next.js | `middleware.ts` | `proxy.ts` da Next.js 16 |
| Trusted Types | Solo Chromium, misura avanzata | Baseline da feb 2026, misura raccomandata |
| Certificati TLS | Calendario incerto | 200 giorni (mar 2026), 100 (mar 2027), 47 (mar 2029) |
| OCSP | Stato incerto | Dismesso da Let's Encrypt il 6/8/2025 |
| pnpm | Comportamento incerto | Script bloccati da v10; usare ≥ 10.26.0 |
| Django | Impostazioni CSP incerte | `SECURE_CSP` nativo in 6.0 |
| Password | Solo Argon2id | Tabella completa OWASP (Argon2id, scrypt, bcrypt, PBKDF2) |
| CRA | Ambito dei servizi online incerto | Criteri RDPS delle linee guida della Commissione |
