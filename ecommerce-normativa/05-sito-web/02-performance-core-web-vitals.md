---
titolo: Performance e Core Web Vitals
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F28, F29]
---

# Performance e Core Web Vitals

## Soglie attuali (75° percentile degli utenti reali) [F28][F29]
| Metrica | Cosa misura | Buono | Da migliorare | Scarso |
|---------|-------------|-------|---------------|--------|
| **LCP** | Velocità di caricamento del contenuto principale | ≤ 2,5 s | 2,5–4,0 s | > 4,0 s |
| **INP** | Reattività alle interazioni (ha sostituito FID il 12/3/2024) | ≤ 200 ms | 200–500 ms | > 500 ms |
| **CLS** | Stabilità visiva (elementi che "saltano") | ≤ 0,1 | 0,1–0,25 | > 0,25 |

Le soglie sono invariate dal passaggio a INP del marzo 2024. Google conferma che i Core Web Vitals sono usati dai sistemi di ranking, ma non come segnale unico. [F28][F29]
> Attenzione a blog che annunciano "nuove soglie più severe": non risultano nella documentazione ufficiale. Usa web.dev come riferimento.

## 🟠 Interventi con il miglior rapporto costo/beneficio
**LCP**
- Immagine "hero" e foto prodotto principali in **AVIF/WebP**, dimensionate correttamente, con `fetchpriority="high"` sull'elemento LCP e **senza** lazy-loading.
- Hosting veloce + **CDN**; TTFB basso. Un hosting lento rovina l'LCP anche con un frontend ottimo.
- Preload dei font critici; `font-display: swap`.

**INP**
- Ridurre il JavaScript: meno app/plugin, script di marketing caricati in modo asincrono o dopo il consenso.
- Spezzare i task lunghi; evitare widget pesanti (chat, recensioni, pop-up) al primo caricamento.

**CLS**
- `width`/`height` (o `aspect-ratio`) su tutte le immagini e gli embed.
- Spazio riservato per banner cookie, barre promozionali, recensioni caricate dopo.

## Misurare
- **Dati reali (field)**: Search Console → Core Web Vitals; PageSpeed Insights (sezione CrUX).
- **Dati di laboratorio**: Lighthouse, WebPageTest — per diagnosticare, non per giudicare.
- Dopo una correzione, i dati CrUX richiedono circa 28 giorni per aggiornarsi.
- Monitorare per **tipo di pagina**: home, categoria, prodotto, carrello, checkout.

## 🟢 Obiettivi interni consigliati
- LCP mobile < 2,0 s sulle schede prodotto.
- Peso pagina prodotto < 2 MB al primo caricamento.
- Budget di performance nel processo di sviluppo: nessuna nuova app senza verifica d'impatto.
