---
titolo: Catalogo e schede prodotto
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F10, F31, N01, N02]
---

# Catalogo e schede prodotto

Il catalogo è il patrimonio che alimenta sito, marketplace, Google Shopping e superfici AI. Dati puliti = più visibilità ovunque. [F31]

## Struttura dati minima per ogni prodotto
| Campo | Obbligatorio per | Note |
|-------|------------------|------|
| SKU interno | gestione | univoco, stabile |
| GTIN/EAN o ISBN | Google, marketplace | fondamentale per l'identificazione |
| Titolo | tutti | chiaro, con attributi chiave (formato, taglia, colore) |
| Descrizione | tutti | originale, utile, scansionabile |
| Caratteristiche essenziali | 🔴 Codice consumo | materiali, misure, compatibilità, contenuto |
| Prezzo IVA inclusa + prezzo precedente più basso a 30 gg se in sconto | 🔴 Omnibus | vedi [02-prezzi](../03-normativa/02-prezzi-promozioni-recensioni.md) |
| Disponibilità e tempi | tutti | per variante |
| Fabbricante, persona responsabile UE, avvertenze, identificativi, immagine | 🔴 GPSR | vedi [05-gpsr](../03-normativa/05-sicurezza-prodotti-gpsr.md) |
| Ricambi/riparabilità/aggiornamenti software (se pertinente) | 🔴 D.Lgs. 30/2026 | vedi [06-green](../03-normativa/06-green-claims-greenwashing.md) |
| Peso e dimensioni con imballo | spedizioni | calcolo costi automatico |
| Categoria Google | feed | tassonomia Google |
| Attributi strutturati | filtri, AI | colore, taglia, formato, lingua, autore… |
| Immagini (min. 3) e alt text | UX, 🔴 accessibilità | sfondo neutro + contesto |

## 🟠 Best practice di contenuto
- Titolo: `Marca + Prodotto + attributo chiave + variante` (es. "Volta la pagina – Romanzo, brossura, 320 pp.").
- Descrizione in 3 blocchi: **cosa è / per chi è** · **dettagli e specifiche** · **cosa c'è nella confezione / spedizione e resi**.
- Rispondere in anticipo alle domande frequenti (dal customer care: le domande ripetute sono i buchi della scheda).
- Recensioni con foto dei clienti; risposte del venditore.

## 🟢 Gestione
- Un unico punto di modifica (PIM o gestionale) sincronizzato con tutti i canali.
- Controllo qualità mensile: prodotti senza immagine, senza GTIN, con descrizione corta, esauriti da > 60 giorni.
- Prodotti esauriti: "avvisami quando torna" + alternative.
