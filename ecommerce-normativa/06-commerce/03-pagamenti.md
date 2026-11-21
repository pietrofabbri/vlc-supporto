---
titolo: Pagamenti
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F34, F37, N05]
---

# Pagamenti

## Il mix italiano (riferimento)
- **Carte** di credito/debito/prepagate: ancora molto diffuse (PostePay è storicamente forte in Italia).
- **Wallet digitali**: a livello globale nel 2025 sono stati il 56% delle transazioni e-commerce (Worldpay, Global Payments Report 2026). [F34]
- **PayPal**: molto radicato e considerato affidabile dagli acquirenti italiani. [F37]
- **Satispay**: wallet italiano con oltre 6 milioni di utenti, tra i metodi più riconoscibili. [F34]
- **Apple Pay / Google Pay**: velocizzano il checkout su mobile.
- **BNPL (paga a rate)**: Klarna, Scalapay, Alma, PayPal Paga in 3 rate, Satispay "Paga in 3". [F34]
- **Bancomat Pay, MyBank, bonifico**: utili per pubblico meno digitale o ordini di valore alto.
- **Wero** (wallet europeo EPI): in espansione, da valutare. [F37]

## 🟠 Best practice
- Offrire **4–6 metodi**: carte + PayPal + Apple/Google Pay + Satispay come base; BNPL se lo scontrino medio supera ~80–100 €.
- Ordine dei metodi adattato al dispositivo (wallet in alto su mobile).
- Per altri Paesi UE: metodi locali (iDEAL in Olanda, Bancontact in Belgio, Blik in Polonia, ecc.) — un gateway unico che li supporti semplifica.
- **Contrassegno**: valutare costi e tasso di rifiuto; se lo offri, indica il sovrapprezzo prima del checkout.
- Valuta i costi reali: commissione % + fissa + cambio valuta + chargeback.

## 🔴 Sicurezza e regole
- **PSD2/SCA**: autenticazione forte del cliente (3-D Secure 2) per i pagamenti con carta nello SEE; le esenzioni sono gestite dal gateway.
- **PCI DSS**: usa campi di pagamento ospitati dal gateway; non conservare mai PAN o CVV.
- **BNPL**: rispetta le informazioni sul credito al consumo; dal recepimento della nuova direttiva sul credito ai consumatori (Dir. 2023/2225, applicazione prevista dal 20/11/2026) anche molti BNPL rientrano nelle tutele — verificare con il provider.
- Rimborsi da recesso: entro 14 giorni, stesso metodo di pagamento.

## Gestione
- Riconciliazione automatica incassi ↔ ordini ↔ contabilità.
- Monitorare: tasso di autorizzazione, tasso di chargeback, frodi.
