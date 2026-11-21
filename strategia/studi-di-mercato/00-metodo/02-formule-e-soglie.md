# 02 · Formule e soglie

[← Griglia](01-griglia-parametri.md) · [Gerarchia fonti →](03-gerarchia-fonti-e-prove.md)

Formule semplici, da calcolare per **tre scenari** (pessimista, base, ottimista). Tutti i prezzi **al netto dell'IVA**.

## 1. Margine di contribuzione

```
Margine unitario (€) = Prezzo netto − Costi variabili unitari
Margine %            = Margine unitario / Prezzo netto
```

**Costi variabili da non dimenticare**: carta (con scarti di avviamento), toner/inchiostro, consumabili di legatura, lamina per doratura, imballo, spedizione, commissioni (marketplace 8–15%, pagamenti 1–3%, MePA 0%), resi, **ore di lavoro diretto** a costo figurativo.

| Soglia | Lettura |
|---|---|
| Margine < 30% | Solo se il volume è alto e automatizzato |
| 30–50% | Normale per stampa conto terzi |
| > 50% | Tipico di prodotti a marchio proprio, personalizzazione, pregio |

## 2. Punto di pareggio (break-even)

```
Unità di pareggio al mese = Costi fissi incrementali mensili / Margine unitario
```

Costi fissi **incrementali** = solo quelli che nascono con l'idea (abbonamento software, leasing nuova macchina, quota sito, assicurazione aggiuntiva). Quelli che esistono già (affitto negozio) non si caricano, salvo saturazione della capacità.

**Controllo di realismo**: le unità di pareggio sono **meno del 30% del SOM** mensile stimato? Se no, l'idea è fragile.

## 3. Tempo di recupero (payback)

```
Payback (mesi) = Investimento iniziale netto incentivi / Margine mensile netto a regime
```

Vincolo dichiarato: **utile entro settembre 2027** → payback ≤ 9–10 mesi da un avvio a fine 2026 per votare 4–5 su P12.

## 4. Valore del cliente e costo di acquisizione

```
LTV = Margine medio per ordine × Ordini per anno × Anni di vita del cliente
CAC = Spesa di acquisizione del canale / Nuovi clienti dal canale
```

| LTV / CAC | Lettura |
|---|---|
| < 1 | Si perde su ogni cliente |
| 1–3 | Regge solo se il canale scala |
| > 3 | Sano |

## 5. Costo orario figurativo

Il tempo non è gratis. Valorizzarlo sempre:

```
Costo orario figurativo = (compenso desiderato annuo + contributi) / ore lavorabili annue
```

Se un'idea genera meno del costo orario figurativo **per ora impegnata**, vale solo come riempimento dei mesi vuoti.

## 6. Scenari e sensibilità

| Variabile | Pessimista | Base | Ottimista |
|---|---|---|---|
| Prezzo | −15% | stimato | +10% |
| Volume | −40% | stimato | +30% |
| Costo carta | +15% | stimato | −5% |
| Tempi di avvio | +3 mesi | stimato | −1 mese |

**Valore atteso** = 25% pessimista + 50% base + 25% ottimista.
Un'idea che **perde nello scenario pessimista** va testata prima di qualunque investimento sopra i 2.000 €.

## 7. Dipendenza dai clienti

```
Concentrazione = fatturato del primo cliente / fatturato dell'idea
```

Oltre il **40%** è un rischio da segnare nel blocco I.

## 8. Dall'analisi ai voti dei 9 filtri

| Filtro | Regola indicativa per il voto 5 | Per il voto 1 |
|---|---|---|
| P12 | payback ≤ 6 mesi **e** utile netto del primo anno ≥ 10.000 € nello scenario base; tetto a 3 se il pessimista è in perdita | utile solo dopo 18 mesi, o meno di 1.000 € nel primo anno |
| INV | investimento netto < 2.000 € | > 25.000 € |
| SFO | < 5 ore/settimana a regime | lavoro artigianale quotidiano |
| RIC | > 60% del fatturato da riordini/contratti | tutto una tantum |
| DUR | driver strutturale, mercato stabile o in crescita | dipende da moda o norma transitoria |
| ESP | vendibile in tutta Italia/UE senza presenza fisica | solo Ferrara |
| RIS | nessun rischio con prob×impatto ≥ 12 | due o più rischi ≥ 15 |

FAC e ASS si votano qualitativamente (vedi `valutazione-idee/01-metodo-e-filtri.md`).
