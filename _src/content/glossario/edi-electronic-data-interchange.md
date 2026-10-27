---
term: EDI (Electronic Data Interchange)
slug: edi-electronic-data-interchange
area: tecnologia
sigla: EDI
esteso: Electronic Data Interchange
description: Lo scambio elettronico di documenti commerciali tra sistemi informativi di aziende diverse, in formati standard: ordini, conferme, avvisi di spedizione, fatture.
related: [erp-enterprise-resource-planning, sscc-serial-shipping-container-code, cross-docking, track-and-trace]
updated: 2026-10-27
---
L'EDI sostituisce il documento inviato e ritrascritto con un messaggio strutturato che il sistema del destinatario legge da solo. I formati storici sono EDIFACT (standard ONU, usato in Europa) e X12 (Nord America); nella distribuzione europea si usa il sottoinsieme EANCOM di GS1. I messaggi più usati in logistica: ORDERS (ordine), ORDRSP (risposta all'ordine), DESADV (avviso di spedizione, con gli [SSCC](/glossario/sscc-serial-shipping-container-code/)), RECADV (avviso di ricevimento), INVOIC (fattura), IFTMIN e IFTSTA (istruzione di trasporto e stato della spedizione).

## In pratica

La grande distribuzione e l'industria automobilistica lo richiedono ai fornitori; i vettori lo usano per ricevere le prenotazioni e inviare gli eventi di tracciamento. L'impresa che lo adotta deve mappare i propri dati sui formati del partner (ogni cliente ha le sue "linee guida"), scegliere il canale (rete a valore aggiunto, AS2, SFTP, o un fornitore di servizi EDI che fa da tramite) e gestire gli errori: un messaggio rifiutato va visto e corretto da qualcuno. Oggi convivono con le interfacce API, più flessibili, ma l'EDI resta lo standard dove servono volumi e stabilità.

## Attenzione a

L'EDI è efficace quanto i dati che trasporta: un DESADV inviato dopo l'arrivo del camion, o con quantità diverse da quelle caricate, è peggio di nessun DESADV.

<div class="fonte" markdown="1">
**Fonte.** Standard UN/EDIFACT sul sito [UNECE](https://unece.org/trade/uncefact/introducing-unedifact); EANCOM sul sito [GS1](https://www.gs1.org/standards/edi/eancom).
</div>
