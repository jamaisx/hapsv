from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN

# Definiamo le piattaforme da caricare (nel tuo caso solo sensor)
PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up da Config Flow."""
    # Nota la 's' finale e la lista [PLATFORMS]
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Rimuovi l'integrazione."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
