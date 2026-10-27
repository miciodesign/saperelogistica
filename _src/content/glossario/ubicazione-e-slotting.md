---
term: Ubicazione e slotting
slug: ubicazione-e-slotting
area: magazzino
description: L'ubicazione è l'indirizzo di una posizione di magazzino; lo slotting è il metodo con cui si decide quale articolo mettere in quale ubicazione.
related: [stoccaggio, picking, wms-warehouse-management-system, analisi-abc]
updated: 2026-10-27
---
Ogni posizione di stoccaggio ha un codice, l'ubicazione, costruito di solito per zona, corsia, campata, livello e vano (per esempio A-03-12-2-1). Senza ubicazioni codificate non esiste gestione informatizzata: il sistema deve sapere dove è ogni cosa, non "più o meno in fondo a destra".

## In pratica

Lo *slotting* è l'assegnazione ragionata degli articoli alle ubicazioni. I criteri principali: frequenza di prelievo (gli articoli che escono di più vanno vicino alla spedizione e ad altezza comoda, i cosiddetti *livelli d'oro* tra il ginocchio e la spalla), peso e volume (i pesanti in basso e per primi nel percorso, così finiscono in fondo al pallet), affinità (articoli ordinati spesso insieme vicini tra loro), vincoli (temperatura, pericolosità, incompatibilità). Lo slotting si rifà periodicamente, perché le rotazioni cambiano con le stagioni e i cataloghi.

## Attenzione a

L'etichettatura fisica. Se l'etichetta dell'ubicazione è illeggibile o messa sul vano sbagliato, l'operatore preleva dal posto vicino e il sistema non se ne accorge finché non arriva l'[inventario](/glossario/inventario-ciclico/). Le etichette vanno controllate come la merce.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale; non esiste una norma che imponga un formato di codifica. Lo standard volontario per l'identificazione delle ubicazioni con codice a barre è il GS1 Global Location Number, descritto nelle [specifiche GS1](https://www.gs1.org/standards/id-keys/gln).
</div>
