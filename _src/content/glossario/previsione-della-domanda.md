---
term: Previsione della domanda
slug: previsione-della-domanda
area: supply-chain
description: La stima di quanto si venderà, per articolo e periodo, su cui si basano le decisioni di approvvigionamento, produzione e scorte.
related: [s-and-op, scorta-di-sicurezza, analisi-abc, effetto-frusta]
updated: 2026-10-27
---
La previsione della domanda (*demand forecasting*) è il punto di partenza di tutta la pianificazione: quanto comprare, quanto produrre, quanto tenere in magazzino e dove. Si fa per articolo, per periodo (settimana o mese) e spesso per canale o area, combinando la storia delle vendite con le informazioni che la storia non contiene: promozioni, nuovi clienti, lanci, stagioni anomale.

## In pratica

I metodi statistici di base (medie mobili, livellamento esponenziale, decomposizione stagionale) bastano per la maggior parte degli articoli con storia regolare; quelli più sofisticati aiutano sugli articoli a domanda intermittente o fortemente promozionale. Più del metodo conta il processo: misurare l'errore di previsione (per esempio l'errore percentuale medio assoluto, MAPE, o il *bias*, cioè la tendenza sistematica a sovra o sottostimare) e usarlo per correggere, e far convergere in un'unica previsione le informazioni di vendite, marketing e logistica, cosa che è lo scopo dell'[S&OP](/glossario/s-and-op/).

## Attenzione a

Una previsione serve se viene usata: la previsione "ufficiale" lasciata in un file mentre gli acquisti ordinano a sensazione produce il peggio dei due mondi. E la domanda registrata non è la domanda vera quando ci sono state rotture di stock: le vendite perse non compaiono nello storico.

<div class="fonte" markdown="1">
**Fonte.** Pratica professionale; metodi e metriche descritti nel dizionario [APICS/ASCM](https://www.ascm.org/) e nei manuali di previsione (per esempio Hyndman e Athanasopoulos, *Forecasting: principles and practice*, disponibile in [open access](https://otexts.com/fpp3/)).
</div>
