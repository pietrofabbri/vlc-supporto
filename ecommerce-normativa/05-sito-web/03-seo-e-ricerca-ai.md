---
titolo: SEO e visibilità nelle ricerche con AI
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-01-15
stato: attuale
fonti: [F29, F30, F31]
---

# SEO e ricerca AI

Le persone cercano prodotti sia su Google classico sia in risposte generate (Google AI Mode/AI Overviews, Gemini, ChatGPT, Perplexity, Copilot). Le basi sono le stesse: **contenuti utili, dati strutturati puliti, sito tecnicamente sano**. Il lavoro su performance va tenuto separato da quello per la ricerca AI: sono liste di priorità diverse. [F29]

## 🟠 SEO tecnica
- Sitemap XML aggiornata e inviata a Search Console e Bing Webmaster Tools.
- `robots.txt` che non blocca CSS/JS né pagine prodotto; decidi consapevolmente quali crawler AI consentire.
- Un **canonical** per ogni pagina; gestione di filtri e parametri (faceted navigation) per evitare migliaia di URL duplicati.
- Prodotti esauriti: lasciare la pagina con alternative (se tornano disponibili) oppure 301 verso il prodotto sostitutivo; 410 solo se eliminati per sempre.
- `hreflang` per le versioni lingua/Paese.
- Mobile-first: Google indicizza la versione mobile.

## 🟠 Dati strutturati (schema.org, JSON-LD)
- `Product` + `Offer` (prezzo, valuta, disponibilità), `AggregateRating`/`Review` solo se reali.
- `MerchantReturnPolicy` e `OfferShippingDetails`: tempi e costi di consegna e reso.
- `Organization` (con dati di contatto), `BreadcrumbList`, `FAQPage` dove utile.
- Per l'editoria: `Book` con ISBN, autore, editore, formato.
- Validare con Rich Results Test e controllare gli errori in Search Console.

## 🟠 Contenuti
- Schede prodotto **originali** (non le descrizioni del fornitore): a chi serve, come si usa, misure, materiali, differenze tra varianti.
- Pagine categoria con un breve testo introduttivo utile, non riempitivo.
- Guide e confronti che rispondono a domande reali ("come scegliere…").
- Autore e data visibili sui contenuti editoriali (esperienza e affidabilità).
- Se usi AI per scrivere: revisione umana sempre (vedi [09-ai-act.md](../03-normativa/09-ai-act.md)).

## 🟠 Visibilità sulle superfici AI e shopping
- **Google Merchant Center** con feed completo e aggiornato (GTIN/ISBN, brand, prezzo, disponibilità, spedizione, resi): è la base per apparire nello shopping di Google, anche nelle risposte AI.
- Dati prodotto coerenti tra sito, feed e marketplace: le integrazioni che espongono un catalogo disordinato alle superfici AI vengono penalizzate a favore di cataloghi puliti. [F31]
- Recensioni e menzioni su siti terzi autorevoli contano per essere citati dalle risposte generate.
- Vedi [05-marketplace-e-commerce-agentico.md](../06-commerce/05-marketplace-e-commerce-agentico.md) per i protocolli di checkout agentico.

## SEO locale (se hai un punto vendita)
- Profilo dell'attività su Google completo, orari aggiornati, foto, risposte alle recensioni.
- Dati NAP (nome, indirizzo, telefono) identici ovunque.
- Inventario locale nel Merchant Center per mostrare "disponibile in negozio".

## Misurare
Search Console (impressioni, clic, query), quota di traffico organico sul fatturato, posizionamento delle 20 categorie principali, errori di indicizzazione.
