---
titolo: Strumenti attivi fuori da questo archivio
ultimo_aggiornamento: 2026-11-21
stato: attuale
---

# Strumenti attivi

Oltre ai file di questo archivio esistono alcuni strumenti che lavorano online. Qui c'è l'elenco, con cosa fanno e dove trovarli.

| Strumento | Dove | Cosa fa | Aggiornamento |
|-----------|------|---------|---------------|
| **Registro conformità e-commerce** | Pagina privata su claude.ai (dalla galleria artefatti di Claude) | Un obbligo per riga con stato, responsabile, data di verifica, note e "perché/come". Scheda Questionario collegata. Si condivide dal menu Condividi | A mano o chiedendo a Claude. Copia statica in `04-registro-conformita/registro-conformita.md` |
| **Progetto "Info legislative"** | claude.ai → Progetti | Moduli normativi, checklist, fonti, modelli, quiz, profilo e quadro dell'azienda: disponibili in ogni conversazione del progetto | Dal monitoraggio mensile e su richiesta |
| **Monitoraggio normativo e-commerce** | Attività programmata, il 1° di ogni mese alle 8:56 | Verifica novità su cookie/Digital Omnibus, recesso, green claims, accessibilità, AI Act, imballaggi, GPSR, IVA, credito ai consumatori; aggiorna calendario e moduli nel progetto; report in `ecommerce/monitoraggio/AAAA-MM.md`; avviso push ed email | Automatico |
| **Monitoraggio bandi e dati** | Attività programmata, il 1° e il 15 di ogni mese alle 8:49 | Bandi Regione, Camera di commercio, Invitalia ecc. per il progetto "Info strategiche" | Automatico |
| **Questionario azienda** | `02-azienda/questionario-azienda.html` | File da mandare via email: si apre con doppio clic, salva nel browser, esporta CSV | Versione 2026-10-15c, 77 domande + note per sezione |
| **Skill "verifica-conformita-ecommerce"** | Proposta in conversazione (da salvare dalla scheda di revisione, se non già fatto) | Controlla schede prodotto, sconti, newsletter, pagine e confezioni secondo questa guida | — |

| **Repository GitHub `pietrofabbri/vlc-supporto`** | github.com, cartella `ecommerce-normativa/` | Raccoglie tutta la documentazione, versionata | Su richiesta |

Istruzioni dei monitoraggi, skill e sorgente del registro: [`../12-strumenti/`](../12-strumenti/README.md).

## Come aggiornare questo repository
Chiedi a Claude, nel progetto "Info legislative": "riesporta il registro, prendi l'ultimo monitoraggio e aggiorna il repository vlc-supporto". Il registro online e i report mensili sono la fonte più recente.
