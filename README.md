# PREZZI PSV ITALIA

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

Prende spunto dall'articolo di [Luca Attanasio](https://blackwiz4rd.github.io/projects/2026-01-09-pun-psv-tracking/)

I prezzi hanno cadenza mensile, l'integrazione esegue una lettura dal sito [LuceGasItalia](https://luceegasitalia.it/indici-pun-e-psv/psv/) ogni 12 ore.

## Installazione

### Metodo 1: HACS (Consigliato)
1. Apri HACS nel tuo Home Assistant.
2. Vai nella sezione **Integrazioni**.
3. Clicca sui tre puntini in alto a destra (`...`) e seleziona **Repository personalizzati**.
4. Inserisci l'URL di questo repository GitHub.
5. Clicca su **Aggiungi**.
6. Clicca su **Installa**.
7. Riavvia Home Assistant.

### Metodo 2: Manuale
1. Copia la cartella `custom_components/nome_integrazione/` nella tua directory `config/custom_components/`.
2. Riavvia Home Assistant.

## Configurazione
Nessuna.

<!-- Definizione dei link per i badge -->
[releases-shield]: https://shields.io
[releases]: https://github.com
[commits-shield]: https://shields.io
[commits]: https://github.com
