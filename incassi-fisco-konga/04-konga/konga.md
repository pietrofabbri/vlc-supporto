# Konga

> Verificato il 15/10/2026 · Produttore: **EasyByte Software** (gruppo Converge)
> Fonti: [Brochure Konga (PDF)](https://www.easybyte.it/sites/default/files/BrochureKonga.pdf) · [Caratteristiche comuni](https://www.easybyte.it/it/prodotti/konga-caratteristiche-comuni) · [Prezzi Konga Lite](https://www.easybyte.it/prezzi-konga-lite) · [Manuale contabilità](https://public.easybyte.it/docs/current/contabilita/manuale_contabilita.html) · [Blog Konga – fatturazione elettronica](https://blog.konga.it/2018/12/12/konga-versione-1-6-0-fatturazione-elettronica/) · [kongalib su PyPI](https://pypi.org/project/kongalib) · [konga_scripts su GitHub](https://github.com/easybyte-software/konga_scripts)

Konga resta **l'unica fonte di verità contabile**: Stripe, sito e banca sono fonti di dati che lo alimentano.

## Edizioni

| Edizione | Limiti | Note |
|---|---|---|
| **Lite** (in uso) | 1 ragione sociale, **250 clienti/fornitori**, **250 articoli** | Per ditte individuali e micro-aziende |
| Mono | Come Pro, ma monoutente | Nessun web service |
| Pro | Multiutente, multiazienda, illimitato | Web service, modulo Server |

Moduli: C Contabilità · V Vendite (documenti, RiBa, RID) · M Magazzino · L Legal Solution (fattura elettronica) · A/O Ordini · P Punto vendita · R Centri di costo · T Lotti · S Server · D Database esterno.
Prezzi Lite (IVA esclusa): 90 € a modulo, assistenza 120 €/anno. Upgrade a Mono: 120 € (C, V, L, cifratura) / 50 € (altri). Upgrade a Pro: 390 € (C, V) / 220 € (M, A, O, T, R, P, L).

## Il caso Volta la Carta

| Limite di Lite | Situazione | Rischio |
|---|---|---|
| 250 articoli | 100–250 titoli + cartoleria, oggetti, servizi | 🔴 Alto |
| 250 clienti/fornitori | Università, dipartimenti, enti, aziende, librerie, privati fatturati, fornitori | 🟠 Medio, cresce ogni anno |
| Magazzino | Modulo M non acquistato, ma "magazzino sempre aggiornato" | ❓ Dove si tengono le quantità |
| Più persone | 2–3 persone sullo stesso PC | OK a turno; uso contemporaneo solo con Pro |

**Da fare:** contare articoli e anagrafiche (ogni trimestre); oltre l'80% di un limite, valutare Mono. Per i soli report, Lite basta: bastano gli export CSV/Excel.

## Fatture elettroniche (modulo L, Legal Solution)
- Alla conferma della fattura Konga crea l'XML; stati: `Sospeso` → `Da Inviare` → `In Attesa Esito` → esito SDI.
- Invio e ricezione tramite intermediario (storicamente 2C Solution, ⚠️ verificare quello attuale).
- Fatture passive ricevute in automatico; documenti integrativi **TD16–TD19** (per i TD17) con "Causale/Cliente Registrazioni Integrative".
- Buona pratica: controllare ogni giorno gli scarti; non allegare PDF pesanti all'XML.

## Piano dei conti per gli incassi
Ogni strumento che trattiene soldi è un **conto transitorio**, censito come una banca nell'Archivio Banche Aziendali.

| Conto | Tipo |
|---|---|
| Banca c/c | Banca |
| Stripe c/transitorio | Banca "virtuale" |
| Commissioni su incassi elettronici | Costo |
| Corrispettivi libri (art. 74) · Corrispettivi servizi 22% · Corrispettivi cartoleria 22% | Ricavi |

| Movimento | Dare | Avere |
|---|---|---|
| Vendite Stripe del periodo | Stripe c/transitorio | Corrispettivi |
| Commissioni | Commissioni su incassi elettronici | Stripe c/transitorio |
| Payout | Banca c/c | Stripe c/transitorio |
| Rimborso | Corrispettivi (storno) | Stripe c/transitorio |

**Controllo:** saldo di Stripe c/transitorio in Konga = saldo Stripe alla stessa data. ❓ Da validare: [domanda 10](../03-fisco/domande-commercialista.md).

## Automazione possibile
| Strumento | Cosa permette | Per Volta la Carta |
|---|---|---|
| Export Excel/CSV/JSON | Report esterni | ✅ Basta per i report |
| Import Excel/CSV/JSON | Caricare registrazioni preparate fuori | Riferimento |
| **kongalib** (Python, v2.1.0, set. 2026, Python ≥ 3.10) | Leggere e scrivere nel database tramite un server Konga | Non serve oggi; ⚠️ probabilmente richiede Pro o Konga Server |
| Web service | Integrazioni | Solo Pro |

Non documentati: connettori per Stripe/WooCommerce, import di estratti conto, gestione specifica dell'art. 74.

## Domande per EasyByte
- [ ] Con Lite, cosa succede a 250 articoli o 250 anagrafiche? Si possono archiviare gli articoli fuori catalogo?
- [ ] Intermediario SDI attuale e costi.
- [ ] Codici IVA consigliati per l'art. 74.
- [ ] Esistono connettori per WooCommerce o Stripe? Import di estratti conto bancari?
- [ ] kongalib funziona con Lite o Mono?
