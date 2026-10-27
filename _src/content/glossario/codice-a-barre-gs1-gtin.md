---
term: Codice a barre GS1 e GTIN
slug: codice-a-barre-gs1-gtin
area: tecnologia
sigla: GTIN
esteso: Global Trade Item Number
description: Il sistema di identificazione univoca dei prodotti gestito dall'organizzazione GS1: il GTIN (il "codice EAN" a 13 cifre) identifica l'articolo, i codici GS1-128 e Datamatrix aggiungono lotto, scadenza e quantità.
related: [sscc-serial-shipping-container-code, lotto-e-tracciabilita, rfid, wms-warehouse-management-system]
updated: 2026-10-27
---
Il codice a barre sulle confezioni è quasi sempre un GTIN-13 (storicamente EAN-13): un numero di tredici cifre che identifica un prodotto in modo univoco nel mondo, assegnato dal proprietario del marchio che ha aderito a GS1 nel proprio Paese. Il GTIN-14 identifica le unità logistiche (il cartone da 12, il pallet da 48). Il sistema GS1 definisce anche come codificare altre informazioni: con i codici GS1-128 (barre lineari) o GS1 DataMatrix (bidimensionali), ogni dato è preceduto da un "identificatore di applicazione" (per esempio 10 per il lotto, 17 per la scadenza, 37 per la quantità).

## In pratica

Per un magazzino il vantaggio è leggere invece di digitare: un codice GS1-128 su un cartone permette di registrare articolo, lotto e scadenza con una sola lettura al [ricevimento](/glossario/ricevimento-merce/). Per questo la grande distribuzione e la farmaceutica chiedono ai fornitori etichette GS1 conformi. I codici proprietari (numeri interni) vanno bene dentro un solo magazzino, non tra aziende. GS1 sta promuovendo il passaggio ai codici bidimensionali anche alle casse ("Sunrise 2027").

## Attenzione a

Il GTIN va assegnato dal proprietario del marchio, non inventato: codici "fatti in casa" con prefissi non propri generano collisioni nelle banche dati dei clienti e vengono rifiutati.

<div class="fonte" markdown="1">
**Fonte.** Specifiche generali GS1 sul sito [GS1](https://www.gs1.org/standards/barcodes) e [GS1 Italy](https://gs1it.org/); norma ISO/IEC 15420 (simbologia EAN/UPC) sul sito [ISO](https://www.iso.org/).
</div>
