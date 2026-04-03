from datetime import timedelta
import logging
import requests
from bs4 import BeautifulSoup

from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Questa variabile ora verrà usata da Home Assistant
SCAN_INTERVAL = timedelta(hours=12)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurazione sensori via interfaccia UI."""
    sensors = [
        LuceGasItaliaSensor(
            "PSV Gas", 
            "https://luceegasitalia.it", 
            "€/Smc",
            config_entry.entry_id
        ),
    ]
    async_add_entities(sensors, True)

class LuceGasItaliaSensor(SensorEntity):
    def __init__(self, name, url, unit, entry_id):
        self._name = name
        self._url = url
        self._unit = unit
        self._entry_id = entry_id # ID della configurazione
        self._state = None
        self._history = []
        
        # Questo permette a HA di gestire l'entità (Aree, Rinomina, Icone)
        # Usiamo l'ID dell'entry per garantire l'univocità
        self._attr_unique_id = f"{entry_id}_{name.lower().replace(' ', '_')}"
        
        # Opzionale: Collega il sensore a un "Dispositivo" unico
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": "Luce e Gas Italia",
            "manufacturer": "Luce e Gas Italia",
        }

    @property
    def unique_id(self):
        """Ritorna l'ID univoco dell'entità."""
        return self._attr_unique_id

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def extra_state_attributes(self):
        return {"history": self._history}

    def update(self):
        """
        Metodo invocato da Home Assistant ogni SCAN_INTERVAL.
        Essendo un metodo sincrono (requests), HA lo esegue in un thread separato.
        """
        _LOGGER.debug("Aggiornamento dati per %s...", self._name)
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(self._url, headers=headers, timeout=15)
            # ... (qui tieni la tua logica di scraping con BeautifulSoup) ...
            
            # Esempio semplificato del risultato dello scraping
            # self._state = valore_estratto
            # self._history = lista_estratta
            
        except Exception as e:
            _LOGGER.error("Errore durante l'aggiornamento di %s: %s", self._name, e)
