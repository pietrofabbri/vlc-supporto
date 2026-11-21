# Connettori Google per Claude

Obiettivo: far lavorare Claude **direttamente sul Google Drive** dell'account Volta la Carta, invece che con file in locale.

## Account

- Indirizzo indicato in chat: `voltalacartaferrara@gmail.it`.
- ⚠️ Gli account Gmail finiscono di solito in **@gmail.com**: verificare l'indirizzo esatto al login.
- Il collegamento non passa dall'indirizzo email: si fa con il login Google (OAuth) quando si clicca sul connettore.

## Connettori

| Connettore | A cosa serve | Stato (21/11/2026) |
|---|---|---|
| Google Drive | Cercare, leggere, caricare file | ✅ Attivo |
| Google Docs | Leggere e modificare documenti | ✅ Attivo |
| Google Sheets | Leggere e modificare fogli di calcolo | ✅ Attivo |
| Google Slides | Leggere e modificare presentazioni | ✅ Attivo |
| Gmail | Cercare email, preparare bozze e risposte | ✅ Attivo |
| Google Calendar | Eventi e appuntamenti | ❓ Non visibile in sessione: da collegare o attivare |

## Come si collega / attiva un connettore

1. **Collegare** (una volta sola): dalla scheda del connettore in chat, oppure da claude.ai → Impostazioni → Connettori. Si apre il login Google: accedere con l'account Volta la Carta e autorizzare.
2. **Attivare nella chat**: un connettore collegato può essere spento in una singola chat. Dal menu strumenti accanto alla casella di testo → accendere l'interruttore del connettore.

## Cosa può fare Claude una volta collegato

- Cercare e leggere i file sul Drive.
- Salvare sul Drive i file che crea, invece di lasciarli in locale.
- Modificare documenti, fogli e presentazioni esistenti.
- Con Gmail: cercare messaggi e preparare bozze (l'invio va sempre confermato).

## Da fare

- [ ] Collegare o attivare Google Calendar.
- [ ] Decidere la struttura di cartelle sul Drive.
