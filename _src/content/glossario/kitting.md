---
term: Kitting
slug: kitting
area: magazzino
description: La preparazione in magazzino di un insieme di componenti o prodotti, raggruppati in un unico kit con un proprio codice, pronto per la produzione o per la vendita.
related: [picking, packing, mrp-material-requirements-planning]
updated: 2026-10-27
---
Il kitting trasforma più articoli in un articolo solo: il magazzino preleva i componenti necessari a una lavorazione (kit di produzione) o a una vendita (kit commerciale, per esempio il prodotto più l'accessorio in confezione regalo), li raggruppa e li registra come un nuovo codice. Da quel momento il kit si movimenta come un pezzo unico.

## In pratica

Serve in produzione per consegnare alla linea esattamente ciò che serve per un lotto, senza che l'operatore vada a cercare i pezzi; e nell'e-commerce per vendere combinazioni di prodotti con un solo codice. Richiede una distinta base (la lista dei componenti del kit) mantenuta nel sistema, un'operazione di "assemblaggio" che scarica i componenti e carica il kit, e l'operazione inversa (*de-kitting*) quando il kit non serve più.

## Attenzione a

La tracciabilità dei lotti: se i componenti hanno lotto o scadenza, il kit deve ereditare il lotto più critico e la scadenza più vicina, altrimenti in caso di richiamo non si sa cosa contiene.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale. Per la tracciabilità degli alimenti: art. 18 del Regolamento (CE) 178/2002, su [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2002/178/oj).
</div>
