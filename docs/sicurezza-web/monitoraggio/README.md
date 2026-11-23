# Monitoraggio sicurezza del sito

[← Sicurezza web](../README.md) · [← vlc-supporto](../../../README.md)

Revisione **settimanale** della sicurezza del nuovo rilegaretesi.it ([`voltalacarta/rt2`](https://github.com/voltalacarta/rt2)), che segue il sito man mano che viene costruito. La fa un'attività pianificata di Claude ogni **lunedì mattina**.

## Come funziona

1. Legge i commit di `rt2` arrivati dopo l'ultimo report (il commit analizzato è scritto in cima a ogni report).
2. Riconosce cosa è cambiato: pagine, script, librerie, workflow, endpoint, pagamenti, upload, segreti, configurazione di hosting.
3. Applica le schede della [knowledge base](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web) che riguardano quei cambiamenti.
4. Ripete ogni volta i controlli di base: segreti nel repository, workflow, librerie incluse, header dello staging e, quando esiste, della produzione.
5. Aggiorna la tabella di avanzamento verso il lancio, qui sotto.
6. Scrive un report `AAAA-MM-GG.md` in questa cartella e, se ci sono punti 🔴 nuovi, li aggiunge a [Da fare](../07-da-fare.md).

L'attività **non modifica il codice del sito**: propone le correzioni nel report.

Dal 23/11/2026 tiene anche l'[osservatorio dei componenti](osservatorio-componenti.md): patch, vulnerabilità e accortezze su tutti i componenti di tutti i siti, con un confronto mensile (primo lunedì del mese) e un avviso immediato per i casi gravi. Il controllo degli header è sospeso finché lo staging e la produzione non sono raggiungibili dall'ambiente dell'attività.

## Avanzamento verso il lancio

Profilo del progetto: **C · E-commerce** con moduli **UGC** (upload dei PDF) e **API** (endpoint del Worker). Livello ASVS 5.0 **L2**. Lancio previsto: metà gennaio 2027.

| Area | Controllo chiave | Stato |
| --- | --- | --- |
| Segreti | Nessuna chiave nel repository pubblico; chiavi solo nelle variabili cifrate di Cloudflare | ⏳ Da verificare a ogni report |
| Supply chain | Lockfile, installazioni senza script, action fissate per SHA, librerie incluse aggiornate | ⚠️ Aperto (vedi sotto) |
| Header e CSP | CSP strict, HSTS, `frame-ancestors`, `nosniff`, `Referrer-Policy`, COOP | ⏳ In produzione via Worker; GitHub Pages non permette header |
| Prezzo | Ricalcolato nel Worker prima del pagamento | ⏳ Previsto, da verificare quando esiste `/api/preventivo` |
| Upload PDF | URL firmati a scadenza, tipo e dimensione verificati lato server, bucket privato, cancellazione a 30 giorni | ⏳ Previsto, da verificare quando esiste `/api/upload` |
| Pagamento | Stripe Checkout ospitato; firma del webhook verificata; idempotenza | ⏳ Previsto, da verificare quando esistono `/api/checkout` e `/api/stripe-hook` |
| Stato ordine | Link `/ordine/:token` con token casuale lungo, nessun dato oltre il necessario | ⏳ Previsto |
| Pannello | `/admin` dietro Cloudflare Access, nessun accesso senza autenticazione | ⏳ Previsto |
| Anti-abuso | Turnstile su contatti e upload; limite di ordini al giorno lato server | ⏳ Previsto |
| Email | SPF, DKIM, DMARC su `rilegaretesi.it` | ⏳ Da verificare al passaggio di dominio |
| Dati personali | Informativa, DPA (Stripe, Cloudflare, Resend), conservazione definita | ⏳ Vedi [ecommerce-normativa](../../../ecommerce-normativa/README.md) |
| Statistiche | Senza cookie (Cloudflare Web Analytics) | ✅ Previsto dall'architettura |
| Checklist pre-lancio | [Voci 🔴](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/checklist/pre-lancio.md) tutte chiuse | ⏳ |

Legenda: ✅ fatto o verificato · ⏳ non ancora costruito o da verificare · ⚠️ problema aperto · 🔴 bloccante per il lancio.

## Stato iniziale (21/11/2026)

Prima lettura del repository, al commit `68fdd25`:

- ✅ L'[architettura di produzione proposta](https://github.com/voltalacarta/rt2/blob/main/docs/architettura-produzione.md) copre già i punti principali: pagamento ospitato da Stripe, prezzo ricalcolato sul server, PDF su R2 con URL firmati e cancellazione a 30 giorni, pannello dietro Cloudflare Access, segreti solo in Cloudflare, statistiche senza cookie.
- ⚠️ Il workflow `pages.yml` installa i font con `npm i` senza lockfile e senza `--ignore-scripts`, in un job che ha i permessi `pages: write` e `id-token: write`. È il rischio descritto in [npm dopo Shai-Hulud](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/06-supply-chain/npm-dopo-shai-hulud.md): meglio versioni fissate e `--ignore-scripts`, oppure font già inclusi nel repository.
- ⚠️ Le action dei workflow sono indicate per tag (`@v4`), non per SHA.
- ℹ️ pdf.js è incluso nel repository alla versione 4.10.38, successiva alla correzione della vulnerabilità nota CVE-2024-4367. Va tenuto aggiornato.
- ℹ️ Lo staging su GitHub Pages non può avere header di sicurezza: accettabile per lo staging, non per la produzione.

## Report

I report settimanali compaiono qui, dal più recente:

| Data | Commit analizzato | Novità |
| --- | --- | --- |
| 21/11/2026 | `68fdd25` | Stato iniziale (sopra) |
