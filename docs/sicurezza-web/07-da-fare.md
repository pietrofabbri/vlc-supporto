# Da fare

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

Aggiornato al 2026-11-21. Spunta e sposta in fondo ciò che è fatto.

## Subito

- [ ] **rilegaretesi.it attuale**: aggiornare WordPress e plugin, togliere quelli inutili, MFA sugli admin, backup provato → [applicazione](03-applicazione-progetti-vlc.md#rilegaretesiit-attuale-finché-resta-online)
- [ ] **Cookie sul sito WooCommerce attuale**: banner di consenso o rimozione di Google Analytics e Meta Pixel → priorità 1 di [ecommerce-normativa](../../ecommerce-normativa/README.md)
- [ ] **voltalacarta.it**: togliere le pagine di prova pubbliche e i duplicati
- [ ] **Account critici** (GitHub, Google, registrar, hosting, Stripe/PayPal): MFA o passkey, codici di recupero nel password manager
- [ ] Confermare una volta che **NIS2 non si applica** a Volta la carta (se si applicasse, la scadenza del 31/10/2026 è già passata)

## Prima del lancio del nuovo rilegaretesi.it (metà gennaio 2027)

Avanzamento aggiornato ogni lunedì nel [monitoraggio del sito](monitoraggio/README.md).

- [ ] `rt2`, workflow `pages.yml`: installare i font con versioni fissate e `--ignore-scripts` (oggi `npm i` senza lockfile) e fissare le action per SHA

- [ ] Scegliere l'hosting di produzione tenendo conto degli header (GitHub Pages non li gestisce)
- [ ] Pagamento solo tramite pagina ospitata dal PSP; verifica della firma dei webhook
- [ ] Caricamento PDF tramite funzione serverless e storage privato; regola di cancellazione dei file
- [ ] Credenziali Google solo lato server
- [ ] Informativa privacy, DPA con i fornitori (Stripe, PayPal, Google, Brevo)
- [ ] Compilare `security.txt` e il piano di risposta agli incidenti con contatti reali
- [ ] Checklist pre-lancio completa nelle voci 🔴 e `check-headers.py` senza errori

## Sulla documentazione

- [ ] **Decisione 0006** in `documentazione`: è ancora `proposto`. Approvarla (→ `accettato`) o scartarla
- [ ] Fissare per SHA le action dei workflow di `documentazione` (oggi sono per tag, contro le regole della stessa base)
- [ ] Progetto Claude "Info tecniche": sostituire la copia della base (v1.2) con un rimando a GitHub
- [ ] Revisione legale dei modelli: capitolato, politica di divulgazione, piano incidenti, registro violazioni
- [ ] Voce **o17** del [registro di conformità](../../ecommerce-normativa/04-registro-conformita/registro-conformita.md) (procedura data breach): partire dal [piano di risposta agli incidenti](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/15-modelli/piano-risposta-incidenti.md) e dal [registro delle violazioni](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/15-modelli/registro-violazioni.csv), già pronti da compilare

## Scadenze nel calendario

| Data | Cosa |
| --- | --- |
| **1 dic 2026** | Il controllo automatico aprirà la prima issue: il file NIS2 scade il 15/12/2026 |
| 15 dic 2026 | Revisione di `nis2-italia.md` (scadenze ACN, ispezioni avviate) |
| 15 gen 2027 | Scadono le revisioni di 14 file (crittografia, supply chain, AI, normativa, CMS) |
| **mar 2027** | Certificati TLS a **100 giorni**: verificare che ogni dominio abbia il rinnovo automatico |
| apr 2027 | Revisione semestrale dei file sugli standard (OWASP, NIST) |
| ott 2027 | Aggiornare `Expires` in ogni `security.txt` pubblicato |
