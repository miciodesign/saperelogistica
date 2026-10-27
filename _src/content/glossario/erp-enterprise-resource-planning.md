---
term: ERP (Enterprise Resource Planning)
slug: erp-enterprise-resource-planning
area: tecnologia
sigla: ERP
esteso: Enterprise Resource Planning
description: Il sistema gestionale integrato dell'impresa: contabilità, acquisti, vendite, produzione, magazzino contabile; con il WMS e il TMS scambia ordini, conferme e movimenti.
related: [wms-warehouse-management-system, tms-transportation-management-system, mrp-material-requirements-planning, edi-electronic-data-interchange]
updated: 2026-10-27
---
L'ERP è il sistema che tiene i conti dell'impresa e i suoi dati anagrafici: clienti, fornitori, articoli, listini, ordini, fatture, giacenze contabili. Nella logistica è la fonte degli ordini di acquisto e di vendita e la destinazione delle conferme: il [WMS](/glossario/wms-warehouse-management-system/) riceve dall'ERP cosa deve arrivare e cosa deve partire, e gli restituisce cosa è arrivato ed è partito davvero; il [TMS](/glossario/tms-transportation-management-system/) riceve le spedizioni e restituisce i costi.

## In pratica

Le aziende piccole usano spesso il solo ERP anche per il magazzino: funziona finché i volumi e la complessità sono bassi (pochi articoli, poche righe al giorno, nessun lotto). Il segnale che serve un WMS dedicato è quando le giacenze dell'ERP non corrispondono più al magazzino e si vive di "sistemazioni". L'integrazione tra i sistemi è il punto delicato di ogni progetto: le interfacce (ordini in uscita, conferme in entrata) vanno specificate, testate e monitorate, con regole chiare su quale sistema ha ragione quando i dati divergono.

## Attenzione a

Le anagrafiche articolo. Dimensioni, peso, confezione, pallettizzazione, codice a barre: se nell'ERP mancano o sono sbagliati, tutto quello che sta a valle (slotting, cartonizzazione, pianificazione dei carichi) lavora male.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale; definizioni coerenti con il dizionario [APICS/ASCM](https://www.ascm.org/).
</div>
