---
term: SSCC (Serial Shipping Container Code)
slug: sscc-serial-shipping-container-code
area: tecnologia
sigla: SSCC
esteso: Serial Shipping Container Code
description: Il codice GS1 di 18 cifre che identifica in modo univoco una singola unità logistica (un pallet, un collo) e permette di collegarla ai dati di spedizione inviati in anticipo.
related: [codice-a-barre-gs1-gtin, packing, track-and-trace, edi-electronic-data-interchange, cross-docking]
updated: 2026-10-27
---
Mentre il [GTIN](/glossario/codice-a-barre-gs1-gtin/) dice *cosa* è un prodotto, l'SSCC dice *quale* unità logistica è questa: ogni pallet o collo ha il suo numero, mai ripetuto. L'etichetta logistica GS1 lo riporta in un codice GS1-128 nella parte bassa, con eventuali altri dati (contenuto, lotto, scadenza, destinatario) sopra. Il mittente comunica in anticipo, con un avviso di spedizione elettronico, cosa contiene ogni SSCC.

## In pratica

Al ricevimento basta leggere l'SSCC per sapere cosa c'è sul pallet senza aprirlo: il sistema confronta con l'avviso di spedizione e registra l'ingresso. È la base del [cross docking](/glossario/cross-docking/) e del ricevimento rapido nella grande distribuzione; i corrieri usano codici analoghi per i colli. L'SSCC si costruisce con una cifra di estensione, il prefisso aziendale GS1 del mittente, un progressivo e una cifra di controllo: serve un prefisso GS1 proprio per generarli.

## Attenzione a

L'SSCC identifica l'unità, non il contenuto: se il pallet viene riaperto e ricomposto, serve un nuovo SSCC, altrimenti il destinatario riceve dati di un pallet che non esiste più.

<div class="fonte" markdown="1">
**Fonte.** Specifiche GS1 per l'etichetta logistica e l'SSCC sul sito [GS1](https://www.gs1.org/standards/id-keys/sscc) e [GS1 Italy](https://gs1it.org/).
</div>
