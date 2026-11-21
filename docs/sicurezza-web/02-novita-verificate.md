# Novità di sicurezza web verificate (2025-2026)

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

Controllate sulle fonti primarie il **2026-10-15**. Sono le informazioni che invecchiano prima: da ricontrollare ogni 3-6 mesi.

## Scadenze e calendari

| Quando | Cosa | Impatto |
| --- | --- | --- |
| mar 2026 ✅ | Certificati TLS pubblici: validità massima **200 giorni** | Già in vigore |
| 11 set 2026 ✅ | CRA: obbligo di segnalare vulnerabilità sfruttate entro 24 h (fabbricanti) | Solo per chi distribuisce prodotti digitali |
| 31 ott 2026 ✅ | NIS2: misure di sicurezza di base operative (soggetti in elenco dal 2025) | Solo per soggetti NIS2 |
| 1 gen – 28 feb 2027 | NIS2: finestra annuale di registrazione ACN | Solo per soggetti NIS2 |
| **mar 2027** | Certificati TLS: validità massima **100 giorni** | Il rinnovo deve essere automatico |
| mar 2028 | Riuso della validazione del dominio: 10 giorni | |
| **mar 2029** | Certificati TLS: validità massima **47 giorni** | Rinnovo manuale impossibile |
| 11 dic 2027 | CRA: applicazione completa e marcatura CE | Solo per fabbricanti |

## Browser

| Funzione | Stato a ottobre 2026 |
| --- | --- |
| **Trusted Types** | Baseline da feb 2026: Chrome/Edge 83+, Safari 26+, Firefox |
| **Sanitizer API** `setHTML()` | Firefox 148, Chrome/Edge 146; **non** Safari. Non confondere con `setHTMLUnsafe()` |
| **DBSC** (sessioni legate al dispositivo) | Chrome, solo Windows (da mag 2026) |
| **TLS post-quantum** `X25519MLKEM768` | Default in Chrome (131+, non disattivabile dalla 138) e Firefox; oltre 2/3 del traffico umano Cloudflare. Standard: RFC 10024 (ago 2026) |
| **Certificati post-quantum** (ML-DSA) | Non ancora disponibili da CA pubbliche |
| **OCSP** | Let's Encrypt lo ha spento il 6/8/2025; i browser usano le CRL. Niente Must-Staple |

## Strumenti e linguaggi

| Strumento | Novità |
| --- | --- |
| **Go** ≥ 1.24 | `X25519MLKEM768` attivo di default (disattivabile con `GODEBUG=tlsmlkem=0`) |
| **OpenSSL** ≥ 3.5 | Supporta il gruppo ibrido post-quantum |
| **Django** 6.0 | CSP nativa: `SECURE_CSP`, `SECURE_CSP_REPORT_ONLY`, costanti `django.utils.csp.CSP` |
| **Next.js** 16 | Il middleware si chiama `proxy.ts`; il nonce CSP si applica da solo ma obbliga al rendering dinamico |
| **pnpm** ≥ 10 | Script delle dipendenze bloccati per default. Usare **≥ 10.26.0** (CVE-2025-69264) |
| **npm** | Dopo Shai-Hulud: 2FA obbligatoria per pubblicare, token di max 7 giorni, trusted publishing via OIDC (npm ≥ 11.5.1) |
| **Dependabot** | Opzione `cooldown`: vale per gli aggiornamenti di versione, non per quelli di sicurezza |
| **OSV-Scanner** v2 | `osv-scanner scan source --recursive <dir>` |

## Attacchi da ricordare

| Evento | Quando | Lezione |
| --- | --- | --- |
| **Shai-Hulud** | set 2025 | Worm npm partito da phishing ai maintainer; rubava token e si ripubblicava. `npm install` = esecuzione di codice |
| **SHA1-Hulud** | nov 2025 | Seconda ondata dello stesso schema |
| **EchoLeak** (CVE-2025-32711) | 2025 | Prompt injection indiretta zero-click in Microsoft 365 Copilot: esfiltrazione con una sola email |

## Normativa: punti chiave

- **NIS2 Italia:** determinazione ACN 379907/2025 con misure di base (37 misure e 87 requisiti per i soggetti importanti, 43 misure e 116 requisiti per gli essenziali). Dal 15/01/2026 la notifica degli incidenti è pienamente operativa. Da ottobre 2026 l'ACN può fare ispezioni.
- **CRA e siti web:** un servizio online rientra solo se è la *soluzione di elaborazione dati remota* di un prodotto. Criteri: è parte integrante, il prodotto ne dipende, lo sviluppa il fabbricante. Un e-commerce non legato a un prodotto distribuito di norma non rientra.

## Fonti principali

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/) · [Indice ASVS 5.0](https://cheatsheetseries.owasp.org/IndexASVS.html) · [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [Calendario certificati 47 giorni (AppViewX)](https://www.appviewx.com/blogs/its-official-ca-b-forum-votes-yes-to-47-day-tls-certificates/) · [Let's Encrypt, fine di OCSP](https://letsencrypt.org/2024/12/05/ending-ocsp.html)
- [Trusted Types (URIports)](https://www.uriports.com/blog/csp-trusted-types/) · [RFC 10024 (PostQuantum.com)](https://postquantum.com/security-pqc/rfc-10024-hybrid-mlkem-tls/) · [Go crypto/tls](https://go.googlesource.com/go/+/HEAD/src/crypto/tls/defaults.go)
- [Next.js CSP](https://nextjs.org/docs/app/guides/content-security-policy) · [Django 6.0 CSP](https://django.readthedocs.io/en/6.0.x/_sources/ref/csp.txt) · [pnpm CVE-2025-69264](https://osv.dev/vulnerability/GHSA-379q-355j-w6rj)
- [GitHub, npm dopo Shai-Hulud (The Hacker News)](https://thehackernews.com/2025/09/github-mandates-2fa-and-short-lived.html)
- [NIS2 31 ottobre 2026 (Pillitteri)](https://pasqualepillitteri.it/news/14825/nis2-scadenza-ottobre-2026-adempimenti) · [CRA art. 14 (Agenda Digitale)](https://www.agendadigitale.eu/sicurezza/cyber-resilience-act-al-via-gli-obblighi-di-notifica-dellarticolo-14/) · [CRA e servizi remoti (DLA Piper)](https://www.dlapiper.com/en/insights/publications/law-in-tech/2026/cyber-resilience-act)

Bibliografia completa: [`25-sicurezza-web/fonti.md`](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/fonti.md).
