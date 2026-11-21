---
titolo: Quadro dell'azienda e piano di lavoro
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-01-15
stato: attuale
fonti_interne:
  - questionario-volta-la-carta-20261015.csv (questionario e-commerce e bandi, compilato da Claudio Fabbri)
  - questionario-titolare-2026-10-15.csv (incassi, Konga, banca)
  - questionario-risposte.csv (attività, macchine, idee)
---

# Quadro dell'azienda e piano di lavoro

> Sintesi delle risposte ai tre questionari del 15/10/2026. Informazione, non consulenza legale o fiscale: le voci fiscali vanno confermate con il commercialista.

## 1. Chi siete, in breve

| Voce | Risposta |
|------|----------|
| Forma e regime | Ditta individuale, contabilità ordinaria, IVA mensile |
| Dimensione | 1–2 persone, fatturato sotto 100.000 € → **microimpresa** |
| Sede | Ferrara (Emilia-Romagna), laboratorio aperto al pubblico, locali in affitto, impresa con più di 10 anni |
| Attività | Casa editrice (oltre 100 titoli in catalogo, circa 11–20 novità l'anno, tutti con ISBN), stampa e rilegatura (500–1.500 tesi l'anno, 25–50% del fatturato), cartoleria e oggetti |
| Clienti | Soprattutto aziende ed enti: università, enti di formazione, comuni, musei, studi professionali. Abilitati al MePA |
| Vendita online | Sito WooCommerce attivo e "importante"; pochi ordini (0–50 al mese), scontrino medio 20–50 €, quasi nessun reso, solo Italia |
| Incassi | Carte (Stripe appena aperto), POS, bonifico (il più usato), contanti. Niente PayPal o Satispay |
| Spedizioni | Un corriere, Poste, ritiro in sede; spedite voi in 1–2 giorni, con imballaggi riusati |
| Amministrazione | Konga Lite con fattura elettronica, conservazione e backup automatici; registratore telematico e POS già collegati; 15–30 ore al mese su incassi e fatture |
| Finanziamenti | Nessun debito ("solo soldi miei"), utile nell'ultimo esercizio, DURC regolare, PEC e firma digitale, nessun aiuto de minimis ricevuto |

## 2. Risposte che non tornano (da chiarire)

| # | Tema | Cosa dicono i questionari | Perché conta |
|---|------|---------------------------|--------------|
| 1 | **Marketplace** | E-commerce: "Altri (IBS, eBay, Etsy…)" · Incassi: Amazon/marketplace "non lo usiamo" · Idee: su Amazon o librerie online "sì, in proprio" | Gli obblighi (dati di sicurezza, recesso, link ODR) valgono anche sui profili venditore |
| 2 | **E-book** | Incassi: "gli e-book hanno l'ISBN: sì, tutti" · E-commerce: "non pubblichi e-book" · Idee: "mai prodotto un EPUB" | Cambia l'ambito accessibilità e i diritti con gli autori (vedi §4) |
| 3 | **ZLS** | Bandi: sede in zona agevolata "No" · Idee: laboratorio nel comune di Ferrara, area ZLS "Sì" | La ZLS riguarda aree precise, non tutto il comune: va controllato l'indirizzo esatto sulla mappa ufficiale della ZLS Emilia-Romagna |
| 4 | Persone | "1–2 persone", ma Konga è usato da 2–3 persone | Se c'è un collaboratore esterno con accesso ai dati, va nominato responsabile del trattamento |

## 3. Piano di lavoro

Ordinato per rischio e facilità. Con poco tempo a disposizione, conviene chiudere un blocco alla volta.

### Subito (1–2 settimane): rischio sanzioni, lavoro breve
1. **Banner cookie.** Oggi non c'è, ma sono attivi Google Analytics e Meta Pixel: è la violazione più facile da contestare. Installare una CMP per WooCommerce con "Rifiuta" ben visibile e bloccare i tracker fino al consenso. Se il Pixel non serve, toglierlo. → registro o15
2. **Condizioni di vendita:** aggiungere le esclusioni dal recesso (rilegature e stampe su misura, lavori personalizzati) e dire chi paga il reso. → o02, o09
3. **Link ODR:** cercarlo nel sito, nelle condizioni e nelle email automatiche di WooCommerce, e toglierlo. → o34
4. **Parole "green"** sul sito: riscriverle in modo specifico e documentabile oppure toglierle (non avete certificazioni). → o23
5. **Schede prodotto:** aggiungere i dati di chi produce. Per i vostri libri basta l'editore con indirizzo ed email (si può mettere una volta nel modello di scheda); per gadget e cartoleria di terzi, il fabbricante. → o21

### Entro un mese
6. **Privacy:** aggiornare l'informativa (Analytics, Meta, Stripe, hosting, corriere, Konga), compilare il registro dei trattamenti, raccogliere gli accordi privacy dei fornitori. → o14, o16
7. **Sicurezza account:** verifica in due passaggi su sito, posta, Stripe e banca; eliminare le password condivise (un gestore di password con accessi personali).
8. **Email dal dominio aziendale** invece di Gmail: le conferme d'ordine arrivano meglio e si riduce il rischio di imitazioni.
9. **Pulsante di recesso:** verificare che abbia i due passaggi e mandi la ricevuta automatica. → o05

### Entro tre mesi (con il commercialista)
10. **Imballaggi e CONAI:** chiarire se l'iscrizione è dovuta e cosa comporta il riuso degli imballaggi. → o26–o28
11. **Indirizzo di ricezione delle fatture** sul sito dell'Agenzia delle Entrate (risposta "non so"). → o30
12. **Fornitori esteri** (Meta, Google, Adobe/Canva, Stripe): è l'adempimento che pesa di più. Le loro fatture richiedono l'integrazione dell'IVA con autofattura elettronica: chiedere al commercialista o a EasyByte se Konga può automatizzarla.
13. **Diritti digitali con gli autori** (vedi §4) prima di qualunque progetto di e-book, audiolibri o uso con AI.

### Opportunità a basso costo
- **Scheda Google dell'attività** (risposta "non so"): con laboratorio aperto e tesi da rilegare, è il canale gratuito più utile.
- **Analytics già installato ma non guardato:** una volta sistemato il consenso, basta un controllo mensile su pagine viste e ordini.
- **Metodi di pagamento:** con pochi ordini non è urgente; se il sito deve crescere, PayPal e Satispay sono i primi da aggiungere.

## 4. Punti di attenzione emersi dalle idee di sviluppo

Solo le implicazioni normative delle idee segnate "Mi interessa". La valutazione delle idee è in [`strategia/valutazione-idee/`](../../strategia/valutazione-idee/00-indice.md).

| Idea | Cosa considerare |
|------|------------------|
| ACC-03 E-book accessibili; ACC-01, ACC-02 | Il vostro catalogo non ha ancora EPUB e i contratti con gli autori **non coprono il digitale**: senza quei diritti non si possono vendere e-book dei titoli esistenti. Per gli e-book prodotti per terzi, l'accessibilità (EAA) è un argomento di vendita, perché i clienti più grandi non sono esenti |
| NEW-04 MePA, DOC-07/11 scuole, UNI-02 | Già abilitati: è il canale più coerente con la clientela. Servono DURC e firma digitale, che avete |
| DOC-01 Manuali e documentazione di conformità | Si collega al GPSR e alle istruzioni obbligatorie dei prodotti: domanda in crescita dalle PMI |
| DOC-09 Diari per pazienti | Se contengono dati sanitari raccolti da voi, attenzione al GDPR (dati particolari); se sono solo stampati per strutture sanitarie, il titolare dei dati resta la struttura |
| NEW-06 Autopubblicazione con marchio separato | Servono condizioni di contratto chiare su diritti, ISBN e responsabilità dei contenuti |
| UNI-01 Sistema ordini tesi in licenza | Se tratta dati di studenti per conto di altre copisterie, voi sareste responsabili del trattamento: contratti privacy e sicurezza |
| EXP-04, DOC-10 Export | Oggi nessuna vendita estera: con vendite a privati UE oltre 10.000 € l'anno scatta l'IVA del Paese del cliente (OSS) |

## 5. Profilo per i bandi

| Requisito tipico | Situazione |
|------------------|-----------|
| Dimensione | Microimpresa (accesso alle riserve per micro e piccole imprese) |
| Regolarità | DURC regolare, PEC e firma digitale presenti |
| Aiuti de minimis | Nessuno negli ultimi 3 anni: plafond pieno |
| Capacità di anticipare | In parte; nessun ricorso a debito |
| Progetti | Sito, e-commerce o software; budget sotto 10.000 € |
| Settore | Editoria (verificare il codice ATECO esatto nella visura: alcuni bandi escludono o premiano settori) |
| Territorio | Emilia-Romagna, Ferrara; ZLS da verificare (§2) |
| Punti deboli | Nessuno che segua le domande; bandi già tentati senza successo; nessuna certificazione |

Indicazione pratica: con budget sotto 10.000 € e nessun debito, sono adatti i **voucher a fondo perduto** per digitalizzazione e formazione (tipicamente Camera di commercio e Regione), che rimborsano una quota delle spese. Il monitoraggio quindicinale dei bandi già attivo può usare questo profilo per filtrare.

## 6. Cosa è stato aggiornato
- Registro di conformità online: 23 obblighi aggiornati (stati e note dal questionario). Esito: 1 fatto (verifica microimpresa), 3 in corso, 10 non applicabili, 21 da fare.
- Questo file e `profilo.md` nella guida; copia nel progetto "Info legislative".
