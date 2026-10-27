# Piano editoriale Sapere Logistica

Regole per chi scrive (persona o sistema automatico). Il sito ha tre prodotti: glossario, rassegna settimanale, corso di aggiornamento. Nessuna firma individuale: si firma "Redazione Sapere Logistica". Nessun link di affiliazione. Monetizzazione: corso + sponsor di settore (regole in `_src/content/pagine/trasparenza.md`).

## Regole comuni

- Tre regole non negoziabili: **fonti ufficiali** (norma, standard, dato di un'amministrazione o di un istituto statistico, linkato), **prezzi verificati** (ogni numero con valore, fonte e data di rilevazione), **correzioni dichiarate** (registro in `_src/content/pagine/correzioni.md`, formato in fondo al file).
- Tono: pratico, diretto, seconda persona quando serve, niente gergo non spiegato, niente elenchi di virtù, niente "nel panorama attuale". Frasi che dicono una cosa.
- Niente notizie quotidiane: la rassegna è settimanale. Niente classifiche di fornitori. Niente articoli sponsorizzati non segnalati. Niente temi fuori perimetro (servizi ambientali, rifiuti, energia, PA e rappresentanza sono di altri siti della redazione).
- Link esterni: il template aggiunge `rel="noopener" target="_blank"`. Un link verso uno sponsor va marcato a mano con `{: rel="sponsored noopener" }` (sintassi attr_list dopo il link).
- Dopo ogni modifica: `python3 _src/build.py` (fallisce se mancano campi o ci sono link interni rotti), controllo visivo delle pagine toccate, commit e push su main. Hostinger pubblica la radice del repo.

## Glossario (`_src/content/glossario/<slug>.md`)

- Un file per voce, nome file = slug. Front matter: `term`, `slug`, `area` (uno degli slug in `config.json` → `aree`), `description` (una frase, è il sottotitolo e la meta description), `related` (lista di slug esistenti, 3-5), `updated` (AAAA-MM-GG), facoltativi `sigla` ed `esteso`.
- Corpo: un paragrafo di definizione; `## In pratica`; `## Attenzione a`; blocco `<div class="fonte" markdown="1">**Fonte.** ...</div>` in fondo. 150-300 parole. Se la definizione è di pratica professionale e non ha una norma dietro, scriverlo nella sezione Fonte.
- Le voci si aggiornano quando cambia la norma: aggiornare testo e `updated`. Se la voce era sbagliata già prima, è una correzione: registro.
- Stato: 92 voci pubblicate il 2026-10-27 (magazzino 14, trasporti 17, supply chain 16, dogane 13, normativa 12, tecnologia 9, indicatori 10).

### Coda voci da scrivere (in ordine)

- [ ] Deposito doganale e perfezionamento attivo · dogane
- [ ] Accise ed e-DAS · dogane
- [ ] Autorità di regolazione dei trasporti (ART) · normativa
- [ ] Trasporto eccezionale · normativa
- [ ] Massa per asse e pesatura · normativa
- [ ] Magazzino fiscale / magazzini generali e fede di deposito · normativa
- [ ] Cassa mobile e semirimorchio gruabile · trasporti
- [ ] Autorità di sistema portuale e terminal · trasporti
- [ ] Short sea shipping e autostrade del mare · trasporti
- [ ] Trasporto ferroviario merci: tracce, operatore, MTO · trasporti
- [ ] Carico di ritorno e borsa carichi · trasporti
- [ ] Kanban · supply chain
- [ ] VMI (vendor managed inventory) · supply chain
- [ ] Postponement · supply chain
- [ ] Resilienza e mappatura dei rischi di fornitura · supply chain
- [ ] Mezzanino e soppalco · magazzino
- [ ] Baia di carico e attrezzature di banchina · magazzino
- [ ] Imballaggio terziario e filmatura · magazzino
- [ ] WCS/WES · tecnologia
- [ ] Telematica di bordo e FMS · tecnologia
- [ ] API e integrazione con i vettori · tecnologia
- [ ] Digital twin e simulazione · tecnologia
- [ ] Perfect order · indicatori
- [ ] Costo per riga e costo per collo · indicatori
- [ ] Emissioni per tonnellata-chilometro (ISO 14083) · indicatori
- [ ] Tasso di infortuni (indici di frequenza e gravità) · indicatori

## Rassegna settimanale (`_src/content/rassegna/AAAA-MM-GG-<slug>.md`)

- Esce il venerdì. Front matter: `title` ("Rassegna della settimana · 3-7 novembre 2026"), `slug` (`2026-11-07`), `date`, `description`.
- Quattro sezioni fisse, nello stesso ordine: `## Norme e regole`, `## Prezzi e indici`, `## Scadenze`, `## Numeri del settore`. Ogni notizia: 2-5 righe, link alla fonte originale nella riga, riferimento esatto (numero, data, articolo) per le norme; valore, fonte e data per i numeri.
- Fonti da passare ogni settimana: Gazzetta Ufficiale (serie generale e UE), EUR-Lex (trasporti, dogane, lavoro), MIT (circolari, decreti, albo), ADM (circolari, determinazioni, Intrastat), Agenzia delle Entrate (risposte su IVA/dogane), Ministero dell'Ambiente (prezzi medi carburanti settimanali), ISTAT ed Eurostat (trasporti, commercio estero), Banca d'Italia, Assoporti/AdSP, ART, Conferenza Stato-Regioni, Confetra/Fedespedi/associazioni autotrasporto.
- Non si pubblica se una settimana non ha almeno 4 notizie con fonte primaria: meglio saltare che riempire.
- Prima uscita: quando il sistema di raccolta fonti è a regime (obiettivo: novembre 2026).

## Corso di aggiornamento (`_src/content/corso/NN-<slug>.md`)

- 12 moduli, programma pubblicato il 2026-10-27. Front matter: `title`, `slug`, `order`, `percorso` (comune / operativo / ufficio), `durata`, `stato`, `description`, `lezioni` (lista; elementi con virgole fra doppi apici).
- Per ogni modulo, quando pronto: lezione scritta (30-45 minuti di lettura), scheda fonti con riferimenti esatti, esercizio su caso reale anonimizzato con soluzione commentata, test di autoverifica. La parte a pagamento non sta nel repo pubblico: nel repo resta la pagina programma; il materiale va sulla piattaforma di erogazione (da scegliere).
- Attestato di partecipazione, non certificazione: scriverlo ovunque, anche sull'attestato.
- Ordine di scrittura: 1, 2, 3 (comuni), poi 4 e 8, poi 9 e 5, poi il resto.
- Prezzo: da definire; finché non è definito, `config.json` → `corso.prezzo` resta vuoto e la pagina dice che sarà pubblicato all'apertura.

## Controlli periodici

- **Controllo mensile prezzi e norme** (primo giorno lavorativo del mese): per ogni voce di glossario che cita un valore o una scadenza (limite CMR in DSP, soglie Intrastat, date del pacchetto mobilità, durata CQC, accordi Stato-Regioni, valori indicativi MIT) riaprire la fonte e confrontare. Aggiornare `updated` solo se cambia qualcosa. Registro qui sotto.
- **Controllo trimestrale link esterni**: script o verifica manuale dei link nelle sezioni Fonte; un link morto si sostituisce con la pagina ufficiale corrente, non con una copia.
- **Dopo ogni edizione ADR (anni dispari), ogni aggiornamento annuale della NC (dicembre) e ogni modifica al Codice della strada**: voci interessate da rileggere.

### Registro controlli

- (nessun controllo ancora eseguito; primo controllo previsto il 3 novembre 2026)

## Da fare prima della messa online definitiva

- [ ] Completare i dati del titolare nella pagina privacy.
- [ ] Decidere se ospitare i font in locale (la privacy lo annuncia).
- [ ] Impostare la casella redazione@saperelogistica.it e il DNS su Hostinger per saperelogistica.it (e il redirect dal .com, se registrato).
- [ ] Google Search Console: aggiungere il file di verifica in `_src/static/` (il build lo copia in radice).
- [ ] Scegliere la piattaforma di erogazione del corso e il sistema di pagamento.
