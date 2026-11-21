# Sicurezza web

[← vlc-supporto](../../README.md)

Sintesi schematica del lavoro sulla sicurezza di siti e app (ottobre-novembre 2026): ricerca sulle best practice 2026, knowledge base, verifica sulle fonti primarie, pubblicazione nella documentazione.

> **Fonte unica:** il testo completo sta in [`voltalacarta/documentazione` → `25-sicurezza-web/`](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web). Questi schemi lo riassumono: in caso di differenza vale la documentazione.

## Mappa

| # | Schema | In una riga |
|---|---|---|
| 1 | [Sintesi delle best practice](01-sintesi-best-practice.md) | Cosa fare, area per area, con le priorità |
| 2 | [Novità verificate 2025-2026](02-novita-verificate.md) | Fatti datati controllati sulle fonti primarie, scadenze |
| 3 | [Applicazione ai progetti VLC](03-applicazione-progetti-vlc.md) | Rischi e controlli per rilegaretesi.it, voltalacarta.it e l'app del second brain |
| 4 | [Strumenti e modelli pronti](04-strumenti-e-modelli.md) | Script, configurazioni e documenti da riusare, e dove trovarli |
| 5 | [Cronologia](05-cronologia.md) | Le tappe del lavoro, versione per versione |
| 6 | [Lezioni apprese](06-lezioni-apprese.md) | Errori trovati e trappole tecniche da ricordare |
| 7 | [Da fare](07-da-fare.md) | Azioni aperte con priorità e scadenze |
| 8 | [Monitoraggio del sito](monitoraggio/README.md) | Revisione settimanale automatica di `rt2`, avanzamento verso il lancio, report |

## Collegamenti nel repository

| Dove | Rapporto con questi schemi |
|---|---|
| [ecommerce-normativa/](../../ecommerce-normativa/README.md) | Obblighi di legge della vendita online (consumo, GDPR e cookie, accessibilità, AI Act…). Qui c'è il lato tecnico, lì quello normativo |
| [ecommerce-normativa/05-sito-web/05-sicurezza-tecnica.md](../../ecommerce-normativa/05-sito-web/05-sicurezza-tecnica.md) | Versione breve, orientata al GDPR art. 32, degli stessi controlli. Coerente con questi schemi |
| [docs/archiviazione.md](../archiviazione.md) | Tipi di storage: utile per decidere dove salvare i PDF degli ordini |

## Legenda priorità

- 🔴 **Obbligatorio**: per qualunque sito in produzione.
- 🟠 **Raccomandato**: per siti con login, dati personali o pagamenti.
- 🟢 **Avanzato**: per rischi alti o requisiti normativi.

## Le tre cose più urgenti

1. Mettere in sicurezza il **rilegaretesi.it attuale** (WordPress): aggiornamenti, plugin inutili rimossi, MFA, backup provato. È il sito che incassa oggi.
2. Prima del lancio del **nuovo rilegaretesi.it** (metà gennaio 2027): pagamento solo su pagina del PSP, PDF su storage privato, credenziali Google solo lato server, hosting che gestisce gli header.
3. Decidere sulla **decisione 0006** della documentazione, ancora `proposto`.
