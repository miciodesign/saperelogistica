---
term: Order cycle time
slug: order-cycle-time
area: indicatori
description: Il tempo che passa tra il ricevimento di un ordine del cliente e la sua consegna; la misura, dal punto di vista del cliente, della velocità dell'intera catena.
related: [lead-time, otif, picking, ultimo-miglio]
updated: 2026-10-27
---
L'order cycle time (tempo di ciclo dell'ordine) è il [lead time](/glossario/lead-time/) visto dal cliente: da quando l'ordine entra nel sistema a quando la merce è a destinazione. Si scompone in fasi, ognuna misurabile: elaborazione e conferma dell'ordine, attesa prima del rilascio al magazzino, prelievo e imballo, attesa del vettore, trasporto, consegna. La scomposizione è la parte utile: dice dove si perde tempo.

## In pratica

Si misura per ordine con le marche temporali dei sistemi (ERP, WMS, TMS, eventi del vettore) e si rappresenta con media e distribuzione: una media di 2 giorni con una coda di ordini a 7 è un problema diverso da una media di 3 giorni stabile. Spesso la fase più lunga non è operativa ma amministrativa: ordini in attesa di verifica del credito, di conferma del prezzo, di un articolo mancante che blocca tutto l'ordine. Le regole di rilascio (spedire quello che c'è o aspettare che l'ordine sia completo) vanno concordate con il commerciale.

## Attenzione a

Promettere un tempo di ciclo in base alla media: il cliente ricorda l'ordine che ha aspettato una settimana, non i venti arrivati in due giorni. L'impegno va preso sul valore che si rispetta nel 95 per cento dei casi.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale; dizionario [APICS/ASCM](https://www.ascm.org/) e modello SCOR (indicatore "Order Fulfillment Cycle Time").
</div>
