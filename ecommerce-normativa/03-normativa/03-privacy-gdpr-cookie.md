---
titolo: Privacy, GDPR e cookie
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2026-12-15   # revisione ravvicinata: Digital Omnibus in negoziazione
stato: da-verificare
ambito: [IT, UE]
si_applica_a: [tutti]
fonti: [F20, F21, F22, F23, N03, N04]
---

# Privacy, GDPR e cookie

## In breve
Oggi valgono **GDPR** (Reg. 2016/679), **Codice privacy** (D.Lgs. 196/2003) e, per i cookie, la direttiva ePrivacy come applicata dal **Garante** (Linee guida cookie del 2021). La riforma "**Digital Omnibus**" proposta dalla Commissione il 19/11/2025 cambierà le regole sui cookie, ma **non è ancora legge**: nel frattempo non cambia nulla. [F20][F23]

## 🔴 Obblighi oggi

**Informativa e basi giuridiche**
- Informativa privacy chiara, raggiungibile da ogni pagina e nei moduli (registrazione, checkout, newsletter, contatti).
- Base giuridica per ogni trattamento: contratto (evadere l'ordine), obbligo legale (fatture), consenso (marketing, profilazione), legittimo interesse (es. soft-spam verso clienti per prodotti analoghi, con opt-out).
- **Registro dei trattamenti** (art. 30) — consigliato anche sotto i 250 dipendenti perché le eccezioni sono strette.
- Nomina dei **responsabili del trattamento** (art. 28): piattaforma e-commerce, hosting, email marketing, corrieri, CRM, chatbot.
- Trasferimenti extra-UE (strumenti USA): verifica adesione al Data Privacy Framework o clausole contrattuali tipo.
- Gestione **data breach**: procedura e notifica al Garante entro 72 ore quando dovuta.
- Diritti degli interessati (accesso, cancellazione, opposizione) evasi entro 1 mese.

**Cookie (regole attuali, Garante 2021)**
- Cookie tecnici: nessun consenso, ma vanno indicati.
- Analytics di terze parti: consenso, salvo configurazioni "anonimizzate" equiparabili ai tecnici secondo i criteri del Garante.
- Marketing/profilazione: **consenso preventivo**; nulla si carica prima della scelta.
- Banner con **"X" o pulsante per rifiutare** facile quanto accettare; niente scroll come consenso; niente dark pattern.
- Non riproporre il banner a chi ha rifiutato prima di 6 mesi (salvo cambi rilevanti).
- Cookie policy con elenco aggiornato.

**Marketing**
- Consenso separato e non pre-spuntato per newsletter e profilazione.
- Double opt-in consigliato come prova del consenso.

## ❓ Digital Omnibus — cosa potrebbe cambiare (stato a ottobre 2026)
- Le regole sui cookie verrebbero spostate dentro il GDPR (nuovo art. 88a), con eccezioni per misurazione di audience di prima parte aggregata. [F23]
- Proposte: rifiuto con un solo clic e periodo minimo prima di riproporre il banner (la bozza del Consiglio di ottobre 2026 lo riduce da 6 a 4 mesi). [F22]
- Il **segnale automatico di consenso dal browser** (art. 88b) è stato **eliminato dal Consiglio il 18/06/2026**: i banner non spariranno. [F21]
- Il fascicolo è ancora in procedura legislativa ordinaria; adozione attesa fine 2026 / 2027, con applicazione circa 6 mesi dopo l'entrata in vigore. [F20]

👉 **Azione:** nessuna modifica obbligatoria oggi; scegli una CMP che si aggiorni automaticamente e preferisci analytics di prima parte, che probabilmente resteranno esenti.

## 🟠 Fortemente consigliato
- **Minimizzazione:** chiedi solo i dati che servono (niente data di nascita obbligatoria se non serve).
- **Conservazione:** definisci tempi (es. dati ordine 10 anni per obblighi fiscali; dati marketing fino a revoca o inattività prolungata).
- **Account cliente:** checkout ospite sempre possibile; l'account è un'opzione.
- Audit annuale dei tag caricati (con strumenti di scansione cookie).

## Collegamenti
- [05-sicurezza-tecnica.md](../05-sito-web/05-sicurezza-tecnica.md)
- [06-email-marketing-crm.md](../06-commerce/06-email-marketing-crm.md)
