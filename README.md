# vlc-supporto

Materiale di supporto per Volta la Carta (Ferrara): appunti tecnici e configurazione degli strumenti.

## Indice

| Documento | Contenuto |
|---|---|
| [docs/archiviazione.md](docs/archiviazione.md) | Infrastruttura per l'archiviazione: tipi di storage, modelli di deployment, aspetti da progettare |
| [docs/connettori-google.md](docs/connettori-google.md) | Lavorare sul Google Drive invece che in locale: connettori Google per Claude e stato del collegamento |

## Decisione chiave

**I file si tengono sul Google Drive dell'account Volta la Carta, non in locale.** Claude lavora sui file attraverso i connettori Google (Drive, Docs, Sheets, Slides, Gmail, Calendar).
