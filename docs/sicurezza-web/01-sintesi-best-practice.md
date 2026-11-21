# Sintesi delle best practice di sicurezza web 2026

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

Una pagina per area. Approfondimenti in [`documentazione/25-sicurezza-web/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web).

## Riferimenti da conoscere

| Standard | Cos'è | Uso |
| --- | --- | --- |
| **OWASP Top 10:2025** | I 10 rischi più diffusi | Linguaggio comune, priorità |
| **OWASP ASVS 5.0** (mag. 2025) | ~350 requisiti testabili in 17 capitoli, livelli L1-L3 | Requisiti di progetto e contratti |
| **OWASP API Security Top 10:2023** | Rischi specifici delle API | Se ci sono API |
| **OWASP Top 10 for LLM 2025** | Rischi delle integrazioni AI | Se c'è un chatbot o un agente |
| **NIST SP 800-63B-4** (lug. 2025) | Regole su password e autenticatori | Login |

## OWASP Top 10:2025 in breve

| # | Rischio | Contromisura chiave |
| --- | --- | --- |
| A01 | Controllo degli accessi (include SSRF) | Verifica lato server di utente **e** proprietà dell'oggetto, su ogni richiesta |
| A02 | Configurazioni errate | Configurazione come codice, debug spento, nulla di esposto |
| A03 | Supply chain del software (**nuova**) | Lockfile, script di installazione spenti, cooldown, SBOM |
| A04 | Crittografia | TLS 1.3, HSTS, Argon2id, segreti in un vault |
| A05 | Injection (include XSS) | Query parametrizzate, escape automatico, CSP strict |
| A06 | Design insicuro | Threat modeling prima di scrivere codice |
| A07 | Autenticazione | Passkey, MFA, password NIST |
| A08 | Integrità di software e dati | CI/CD protetta, artefatti firmati |
| A09 | Log e **alert** | Log centralizzati e qualcuno che riceve gli avvisi |
| A10 | Condizioni eccezionali (**nuova**) | Errori generici, controlli che falliscono "chiusi" |

A01 e A02 sono stati trovati nel **100%** delle applicazioni testate: sono le prime da verificare.

## Per area

### Autenticazione

- 🔴 MFA su tutti gli account amministrativi: sito, hosting, DNS, registrar, GitHub, Google.
- 🟠 **Passkey** come metodo principale: resistono al phishing.
- 🔴 Password: almeno **15 caratteri** (8 se con MFA), nessuna regola di composizione, **nessuna scadenza forzata**, controllo contro le password compromesse, incolla consentito.
- 🔴 Hash: **Argon2id** (m=19 MiB, t=2, p=1 minimo OWASP); bcrypt solo per sistemi esistenti.
- 🔴 Cookie di sessione `Secure; HttpOnly; SameSite=Lax`, ID rigenerato al login, logout lato server.
- ❌ SMS come secondo fattore: solo se non c'è alternativa.

### Autorizzazione e input

- 🔴 Nega per default; controllo di proprietà in ogni query (`WHERE id = ? AND cliente_id = ?`).
- 🔴 Query parametrizzate; validazione con schema; niente `eval` o deserializzazione di dati non fidati.
- 🔴 Escape automatico del framework; HTML degli utenti solo tramite DOMPurify.
- 🔴 Upload: allowlist di tipi verificata sui byte, limite di dimensione, rinomina, fuori dalla web root.
- 🔴 Fetch di URL lato server: blocca IP privati e metadata cloud (SSRF).

### Browser e trasporto

| Header | Valore |
| --- | --- |
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains` |
| `Content-Security-Policy` | Base: `frame-ancestors 'self'; object-src 'none'; base-uri 'self'`. Strict: nonce o hash + `'strict-dynamic'` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Cross-Origin-Opener-Policy` | `same-origin` |
| `Permissions-Policy` | Disattiva fotocamera, microfono, geolocalizzazione se non servono |

- 🔴 TLS 1.3 (1.2 solo con cifrari moderni), certificati a **rinnovo automatico**.
- 🟠 Trusted Types (ora supportato da tutti i browser principali) per i siti con dati sensibili.
- 🟠 Scambio di chiavi post-quantum `X25519MLKEM768` sul server.
- 🔴 CORS: nessuno, o allowlist esatta. Mai riflettere l'origine.

### Supply chain

- 🔴 `npm ci` dal lockfile; script di installazione disattivati (`ignore-scripts=true`, o pnpm ≥ 10.26).
- 🟠 Cooldown di qualche giorno sulle nuove versioni (Dependabot `cooldown`, Renovate `minimumReleaseAge`).
- 🔴 Secret scanning; un segreto finito in un commit si **revoca**, non basta cancellarlo.
- 🔴 Azioni GitHub fissate per SHA, `permissions` minimi, OIDC al posto di chiavi statiche.
- 🔴 SRI sugli script da CDN; pochi script di terze parti.

### Operazioni

- 🔴 Errori generici all'utente; ogni controllo di sicurezza fallisce in modo chiuso.
- 🔴 Log di login, accessi negati, azioni admin; senza password, token o dati sensibili.
- 🔴 Backup 3-2-1-1-0: una copia immutabile, ripristino **provato**.
- 🟠 Piano di risposta agli incidenti con i termini di notifica (sotto).
- 🟠 `/.well-known/security.txt` e politica di divulgazione.

### AI e LLM

- 🔴 Output del modello trattato come input non fidato.
- 🔴 Nessun segreto nel system prompt; permessi minimi agli strumenti; conferma umana per azioni irreversibili.
- 🔴 Prompt injection **indiretta**: anche pagine, file e email letti dal modello possono contenere istruzioni.

## Termini di notifica

| Norma | A chi | Termine | Si applica a VLC? |
| --- | --- | --- | --- |
| GDPR art. 33 | Garante Privacy | **72 ore** | ✅ Sì, per violazioni di dati personali con rischio |
| NIS2 (D.Lgs. 138/2024) | CSIRT Italia | 24 h preallarme, 72 h notifica | Probabilmente no: verificare (vedi [applicazione](03-applicazione-progetti-vlc.md#normativa)) |
| Cyber Resilience Act art. 14 | ENISA + CSIRT | 24 h preallarme | No, finché non si distribuisce software |

## Profili di progetto

| Profilo | Esempio | ASVS | Pen test |
| --- | --- | --- | --- |
| A · Vetrina | Sito istituzionale, catalogo | L1 | Facoltativo |
| B · Area utenti | Area riservata, community | L2 | Prima del lancio |
| C · E-commerce | Negozio, prenotazioni a pagamento | L2 | Prima del lancio + annuale |
| D · Dati sensibili | Sanità, minori, documenti | L2 + parti L3 | A ogni rilascio rilevante |

Moduli aggiuntivi: **UGC** (upload e contenuti degli utenti), **API**, **AI**, **CRA**, **NIS2**.
