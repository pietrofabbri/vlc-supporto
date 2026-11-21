---
titolo: Architettura e scelta della piattaforma
ultimo_aggiornamento: 2026-10-15
prossima_revisione: 2027-04-15
stato: attuale
fonti: [F26, F30, F31]
---

# Architettura e piattaforma

## Scegliere la piattaforma: criteri
| Criterio | Domanda da porsi |
|----------|------------------|
| Costo totale (TCO) | Canone + commissioni sul transato + app/plugin + sviluppo + manutenzione su 3 anni |
| Conformità UE | Supporta pulsante di recesso, prezzo minimo 30 gg, campi GPSR, OSS/IVA per Paese, CMP? |
| Accessibilità | Il tema/checkout è conforme WCAG 2.1/2.2 AA? |
| Prestazioni | Core Web Vitals reali di negozi esistenti sulla stessa piattaforma |
| Integrazioni italiane | Fatturazione elettronica/SdI, corrieri italiani, Satispay, PayPal, Bancomat Pay |
| Canali | Marketplace, Google Merchant Center, social, superfici AI (feed e protocolli) |
| Proprietà dei dati | Esportazione completa di prodotti, clienti, ordini |
| Lingue e valute | Multilingua nativo con URL separati per lingua |

## Famiglie di soluzioni
- **SaaS hosted** (Shopify, BigCommerce, ecc.): veloce da avviare, aggiornamenti e sicurezza inclusi; Shopify ha attivato di default gli "Agentic Storefronts" per esporre il catalogo alle superfici AI. [F31]
- **Open source self-hosted** (WooCommerce, PrestaShop, Magento/Adobe Commerce): controllo totale, ma manutenzione, sicurezza e performance sono a tuo carico.
- **Headless/composable**: frontend separato dal motore commerce; ha senso con team tecnico e volumi alti.

> Contesto italiano: le imprese con un sito e-commerce attivo sono circa 87.000, in calo del 4,4% sull'anno precedente — il mercato premia chi è strutturato, non chi è solo presente. [F27]

## 🟠 Principi di architettura
- **Un dominio principale** con HTTPS, versioni lingua in sottocartelle (`/it/`, `/de/`, `/fr/`) e `hreflang`.
- **URL parlanti e stabili** (`/libri/narrativa/titolo-libro`); redirect 301 per ogni URL cambiato.
- **Catalogo come fonte unica** (PIM o gestionale) che alimenta sito, marketplace e feed.
- Ambiente di **staging** per testare modifiche prima della pubblicazione.
- **Backup** automatici giornalieri, conservati fuori dal server, con test di ripristino.
- Evitare plugin superflui: ognuno è un rischio di sicurezza e un peso sulle prestazioni.

## Collegamenti
- [02-performance-core-web-vitals.md](02-performance-core-web-vitals.md)
- [05-marketplace-e-commerce-agentico.md](../06-commerce/05-marketplace-e-commerce-agentico.md)
