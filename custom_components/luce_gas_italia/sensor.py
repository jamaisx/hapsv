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
        LuceGasItaliaSensor("PSV Gas", "https://luceegasitalia.it", "€/Smc"),
    ]
    # 'True' forza il primo aggiornamento immediato al caricamento
    async_add_entities(sensors, True)

class LuceGasItaliaSensor(SensorEntity):
    def __init__(self, name, url, unit):
        self._name = name
        self._url = url
        self._unit = unit
        self._state = None
        self._history = []
        # Unique ID è fondamentale per gestire l'entità dall'interfaccia
        self._attr_unique_id = f"{DOMAIN}_{name.lower().replace(' ', '_')}"

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
