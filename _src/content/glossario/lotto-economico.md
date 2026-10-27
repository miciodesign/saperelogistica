---
term: Lotto economico
slug: lotto-economico
area: supply-chain
description: La quantità da ordinare ogni volta che minimizza la somma tra il costo di emissione degli ordini e il costo di mantenimento della scorta.
related: [punto-di-riordino, indice-di-rotazione-delle-scorte, costo-logistico]
updated: 2026-10-27
---
Ordinare poco e spesso costa in ordini, trasporti e ricevimenti; ordinare tanto e di rado costa in capitale immobilizzato, spazio e rischio di obsolescenza. Il lotto economico (EOQ, *economic order quantity*) è la quantità che bilancia i due costi, calcolata con una formula che usa la domanda annua, il costo fisso di un ordine e il costo annuo di mantenere a scorta un'unità.

## In pratica

La formula classica è la radice quadrata di (2 × domanda annua × costo per ordine) diviso il costo unitario di mantenimento. Il risultato va preso come ordine di grandezza, non come numero esatto: la curva del costo totale è piatta vicino al minimo, quindi arrotondare a un multiplo di confezione, di pallet o di carico completo cambia poco il costo e semplifica molto la vita. Il valore del costo di mantenimento (di solito tra il 15 e il 30 per cento annuo del valore della merce, tra capitale, spazio, assicurazione e deperimento) è la variabile più incerta e va stimata con onestà.

## Attenzione a

La formula assume domanda costante e prezzo fisso. Con sconti quantità, stagionalità o scadenze va corretta o sostituita da un calcolo esplicito dei costi per ogni alternativa.

<div class="fonte" markdown="1">
**Fonte.** Modello di Harris-Wilson (1913-1934), descritto in ogni manuale di gestione delle scorte; dizionario [APICS/ASCM](https://www.ascm.org/).
</div>
