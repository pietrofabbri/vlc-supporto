---
titolo: Sicurezza tecnica del sito
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [N03, N05]
---

# Sicurezza tecnica

Il GDPR (art. 32) richiede misure tecniche adeguate al rischio; un e-commerce che tratta dati di clienti e pagamenti è un bersaglio frequente.

## 🔴 Minimi indispensabili
- **HTTPS** ovunque, certificato rinnovato automaticamente, HSTS attivo.
- **Pagamenti esternalizzati** a un gateway certificato PCI DSS (campi carta in iframe o pagina ospitata): non conservare mai i dati delle carte.
- **Autenticazione a due fattori** per tutti gli account amministrativi (piattaforma, hosting, dominio, email, gateway).
- **Aggiornamenti** tempestivi di CMS, temi e plugin; rimuovere ciò che non si usa.
- **Backup** giornalieri cifrati e fuori sede, con test di ripristino almeno trimestrale.
- Principio del **minimo privilegio**: ogni collaboratore ha solo i permessi necessari; account nominativi, non condivisi.
- Procedura **data breach** (chi fa cosa, notifica al Garante entro 72 ore quando dovuta).

## 🟠 Fortemente consigliato
- **WAF/CDN** con protezione da bot e DDoS.
- Protezione dei moduli (login, registrazione, contatti) da credential stuffing e spam, con CAPTCHA accessibili.
- Intestazioni di sicurezza: Content-Security-Policy, X-Content-Type-Options, Referrer-Policy.
- Controllo degli **script di terze parti** sul checkout (attacchi tipo "skimming" via script iniettati).
- Monitoraggio uptime e alert.
- Email del dominio protette con SPF, DKIM e DMARC (anche contro il phishing che usa il tuo nome) — vedi [06-email-marketing-crm.md](../06-commerce/06-email-marketing-crm.md).
- Formazione del personale sul phishing.

## 🟢 Buone pratiche
- Antifrode del gateway attivo (3-D Secure/SCA, regole su ordini anomali).
- Registro accessi amministrativi conservato.
- Penetration test annuale per siti con volumi rilevanti.
- Valutare se l'azienda rientra nella NIS2 (D.Lgs. 138/2024): di norma riguarda medie/grandi imprese in settori specifici, ma verifica con il consulente.
