# Lezioni apprese

[← Sicurezza web](README.md) · [← vlc-supporto](../../README.md)

## Sul metodo

| Lezione | Perché |
| --- | --- |
| Verificare i fatti datati sulla **fonte primaria** | Una fonte secondaria diceva il contrario del sorgente di Go |
| Segnare l'incertezza con `⚠️ da verificare` | Rende i punti da controllare ricercabili e contabili |
| Una sola copia viva dei documenti | La copia nel progetto Claude è invecchiata il giorno dopo; GitHub è la fonte unica |
| Mettere una data di revisione su ogni file | La parte normativa e quella sugli strumenti invecchiano in 3-6 mesi |
| Testare gli script su un caso buono **e** su uno volutamente sbagliato | Solo così si vede che segnalano davvero i problemi |

## Trappole tecniche

| Trappola | Cosa succede | Come evitarla |
| --- | --- | --- |
| Segnaposto negli URL (`https://[DOMINIO]/…`) | lychee lo considera un URL non valido anche offline e fa fallire la CI | Scrivere i segnaposto come testo o codice, non come link |
| `markdownlint --fix` sugli elenchi numerati | Rinumera da 1 gli elenchi spezzati da titoli | Usare codici (A1, B2…) quando i numeri devono restare univoci |
| `hashFiles()` nell'`if` di un **job** GitHub Actions | Non è disponibile a quel livello | Metterlo nell'`if` degli step |
| Espressioni regolari in Caddy | Sono RE2: niente lookahead `(?!…)` | Usare matcher con `not` |
| `add_header` in nginx dentro una `location` | Cancella gli header ereditati | Centralizzare gli header in un file incluso |
| `ignore-scripts=true` in npm | Blocca anche gli hook `pre`/`post` degli script del progetto | Eseguire esplicitamente ciò che serve (`npm rebuild <pacchetto>`) |
| Dependabot `cooldown` | Non ritarda gli aggiornamenti di sicurezza | È il comportamento voluto: non serve un'eccezione |
| Nonce CSP in Next.js | Obbliga tutte le pagine al rendering dinamico | Se serve il sito statico: CSP con hash e SRI sperimentale |
| GitHub Pages | Non permette header HTTP personalizzati | CSP via `<meta>`, oppure un hosting che gestisce gli header |

## Sull'ambiente di lavoro cloud

- Alcuni servizi possono non essere raggiungibili dalla sessione (registro npm a tratti, crates.io, download dei log di GitHub Actions). Le **annotazioni** dei job restano leggibili via API e indicano almeno quale step è fallito.
- Il sorgente di uno strumento (es. lychee) si può leggere anche quando non si può compilarlo: basta per capire cosa considera errore.
- Prima di pushare su un repository con regole proprie si leggono `CLAUDE.md` e le convenzioni, e si eseguono gli stessi controlli della sua CI.
