# Infrastruttura per l'archiviazione

Insieme di hardware, software e architetture che servono a conservare, proteggere e rendere accessibili i dati.

## Tipi di storage

| Tipo | Esempi | Quando usarlo |
|---|---|---|
| **A blocchi** (block storage) | SAN, volumi cloud (AWS EBS) | Database e macchine virtuali; servono basse latenze |
| **A file** (file storage) | NAS, NFS, SMB | Cartelle condivise tra persone o server; il più semplice |
| **A oggetti** (object storage) | S3, Azure Blob, MinIO, Google Drive* | Backup, archivi, media, data lake; scala quasi all'infinito |

\* Google Drive non è object storage in senso stretto, ma per l'uso quotidiano ne ha le caratteristiche: in cloud, accessibile ovunque, senza manutenzione.

## Modelli di deployment

| Modello | Pro | Contro |
|---|---|---|
| **On-premise** | Controllo totale, costi prevedibili | Manutenzione e competenze interne |
| **Cloud** | Elastico, a consumo, nessun hardware | Costi di uscita dati (egress) da tenere d'occhio |
| **Ibrido** | Dati "caldi" in locale, archivio/backup in cloud | Più complesso da gestire |

**Scelta per Volta la Carta:** cloud, su Google Drive (vedi [connettori-google.md](connettori-google.md)).

## Aspetti da progettare

- **Ridondanza** — RAID, replica, erasure coding. Su Google Drive se ne occupa Google.
- **Backup: regola 3-2-1** — 3 copie, su 2 supporti diversi, 1 fuori sede, possibilmente immutabile contro i ransomware.
  - Attenzione: il Drive *sincronizzato* non è un backup; se un file viene cancellato o cifrato, la modifica si propaga. Serve una seconda copia indipendente.
- **Tiering** — spostare i dati poco usati su storage più economico (hot → cool → archive).
- **Sicurezza e conformità** — cifratura, controllo degli accessi (chi vede cosa sul Drive), GDPR.
- **Prestazioni** — IOPS, throughput e latenza in base al carico di lavoro; poco rilevanti per un uso documentale.

## Domande aperte

- Quanti dati ci sono da archiviare e di che tipo?
- Serve un backup del Drive su un secondo supporto (regola 3-2-1)?
- Chi deve avere accesso a quali cartelle?
