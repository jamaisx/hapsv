"""Integrazione Luce e Gas Italia."""
import logging

_LOGGER = logging.getLogger(__name__)
DOMAIN = "luce_gas_italia"

async def async_setup(hass, config):
    """Set up del componente via YAML (opzionale)."""
    return True