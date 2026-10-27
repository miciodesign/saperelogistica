---
term: Track and trace
slug: track-and-trace
area: trasporti
description: Il tracciamento di una spedizione lungo il viaggio (track) e la ricostruzione a posteriori del suo percorso (trace), tramite eventi registrati a ogni passaggio.
related: [corriere-espresso, sscc-serial-shipping-container-code, tms-transportation-management-system, edi-electronic-data-interchange]
updated: 2026-10-27
---
Ogni volta che un collo o un'unità di carico viene letta, in ritiro, in hub, in consegna, il sistema del vettore registra un evento con data, ora, luogo ed esito. L'insieme di questi eventi è la tracciabilità della spedizione: permette al mittente e al destinatario di sapere dove è la merce e, in caso di problema, di capire dove si è fermata o persa.

## In pratica

La qualità del tracciamento dipende da due cose: che il codice sia letto davvero a ogni passaggio (un codice illeggibile genera un "buco" negli eventi) e che gli eventi abbiano un significato condiviso. Gli stati tipici: presa in carico, in transito, in consegna, consegnato, tentativo fallito, giacenza, reso al mittente. I vettori espongono gli eventi tramite interfacce (API) o scambi [EDI](/glossario/edi-electronic-data-interchange/) che un [TMS](/glossario/tms-transportation-management-system/) può leggere per aggiornare i clienti senza intervento manuale. La prova di consegna (POD), con firma o foto, è l'evento che chiude la spedizione e fa partire la fattura.

## Attenzione a

Il tracciamento non è una prova dello stato della merce: dice che il collo è passato, non che era integro. Per il danno valgono le riserve sul documento di trasporto.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale. Standard per gli eventi di tracciabilità: GS1 EPCIS, sul sito [GS1](https://www.gs1.org/standards/epcis).
</div>
