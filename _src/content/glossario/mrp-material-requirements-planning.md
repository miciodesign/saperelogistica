---
term: MRP (Material Requirements Planning)
slug: mrp-material-requirements-planning
area: supply-chain
sigla: MRP
esteso: Material Requirements Planning
description: Il metodo che calcola cosa ordinare e produrre, in che quantità e quando, a partire dal piano dei prodotti finiti, dalla distinta base e dalle scorte disponibili.
related: [punto-di-riordino, lead-time, erp-enterprise-resource-planning, kitting]
updated: 2026-10-27
---
L'MRP parte dal piano principale di produzione (quanti prodotti finiti servono e quando), lo "esplode" attraverso la distinta base (l'elenco dei componenti di ogni prodotto, con le quantità) e, tenuto conto delle scorte e degli ordini già aperti, calcola i fabbisogni netti di ogni componente. Poi li sposta indietro nel tempo del [lead time](/glossario/lead-time/) per ottenere le date in cui gli ordini vanno emessi.

## In pratica

È il metodo adatto agli articoli a *domanda dipendente*, cioè che servono solo perché servono i prodotti di cui fanno parte: componenti, semilavorati, materie prime. Per questi il [punto di riordino](/glossario/punto-di-riordino/) non va bene, perché la domanda non è regolare ma arriva a blocchi, quando parte un lotto di produzione. L'MRP è il cuore dei moduli di produzione degli [ERP](/glossario/erp-enterprise-resource-planning/); la sua estensione che considera anche la capacità delle risorse si chiama MRP II.

## Attenzione a

L'MRP è esatto quanto i suoi dati: distinte base sbagliate, lead time di anagrafica non aggiornati e giacenze non corrispondenti al vero producono ordini sbagliati con grande precisione. La pulizia dei dati anagrafici vale più di qualunque algoritmo.

<div class="fonte" markdown="1">
**Fonte.** Dizionario [APICS/ASCM](https://www.ascm.org/); il metodo è descritto nei lavori di Joseph Orlicky (*Material Requirements Planning*, 1975).
</div>
