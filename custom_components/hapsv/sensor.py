import logging
from datetime import timedelta
import requests
from bs4 import BeautifulSoup

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.event import async_track_time_interval

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=12) # Controlla i dati ogni 12 ore

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Configurazione dei sensori."""
    sensors = [
        LuceGasItaliaSensor("PSV Gas", "https://luceegasitalia.it/indici-pun-e-psv/psv/", "€/Smc"),
        # Puoi aggiungere qui il sensore PUN in futuro puntando alla sua URL
    ]
    async_add_entities(sensors, True)

class LuceGasItaliaSensor(SensorEntity):
    def __init__(self, name, url, unit):
        self._name = name
        self._url = url
        self._unit = unit
        self._state = None
        self._history = []

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
        """Metodo per recuperare i dati (Scraping)."""
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(self._url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            matrix = []
            table = soup.find('table')
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    data = [cell.get_text(strip=True).replace('\xa0', ' ') for cell in cells]
                    if len(data) >= 2 and "MESE" not in data[0]:
                        try:
                            p_float = float(data[1].replace(',', '.'))
                            matrix.append({"month": data[0], "price": p_float})
                        except ValueError:
                            continue
            
            if matrix:
                self._state = matrix[0]["price"]
                self._history = matrix
                _LOGGER.debug("Dati aggiornati per %s", self._name)
        except Exception as e:
            _LOGGER.error("Errore durante lo scraping di %s: %s", self._name, e)