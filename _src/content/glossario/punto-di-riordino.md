---
term: Punto di riordino
slug: punto-di-riordino
area: supply-chain
description: Il livello di giacenza al quale si emette un nuovo ordine di approvvigionamento, in modo che la merce arrivi prima che la scorta si esaurisca.
related: [scorta-di-sicurezza, lead-time, lotto-economico, mrp-material-requirements-planning]
updated: 2026-10-27
---
Il punto di riordino (*reorder point*) è il livello di scorta che fa scattare l'ordine. Si calcola come domanda media durante il [lead time](/glossario/lead-time/) più la [scorta di sicurezza](/glossario/scorta-di-sicurezza/): quando la giacenza scende sotto quel valore, si ordina, e la quantità ordinata arriva, in teoria, quando la giacenza tocca la scorta di sicurezza.

## In pratica

È il metodo più semplice di gestione a scorta, adatto ad articoli con domanda regolare e indipendente (ricambi, materiali di consumo, prodotti finiti a catalogo). Un esempio: un articolo vende 10 pezzi al giorno, il fornitore consegna in 15 giorni, la scorta di sicurezza è di 40 pezzi: il punto di riordino è 10 × 15 + 40 = 190 pezzi. Il metodo funziona solo se la giacenza che il sistema vede è quella vera, il che rimanda all'[accuratezza inventariale](/glossario/accuratezza-inventariale/). Per articoli la cui domanda dipende da un piano di produzione, il metodo giusto è l'[MRP](/glossario/mrp-material-requirements-planning/), non il punto di riordino.

## Attenzione a

Gli ordini già emessi e non ancora arrivati vanno contati: il confronto si fa tra punto di riordino e "posizione di scorta" (giacenza più ordini in arrivo meno impegni), non con la sola giacenza fisica, altrimenti si ordina due volte.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale; dizionario [APICS/ASCM](https://www.ascm.org/).
</div>
