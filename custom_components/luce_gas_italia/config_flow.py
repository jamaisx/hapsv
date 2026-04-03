from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class LuceGasItaliaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestisce il setup guidato dell'integrazione."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Primo step: l'utente clicca su aggiungi."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="Luce e Gas Italia", data={})

        return self.async_show_form(step_id="user")
