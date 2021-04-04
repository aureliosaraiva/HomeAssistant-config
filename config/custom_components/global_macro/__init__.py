import logging
from homeassistant.helpers.template import Template


_LOGGER = logging.getLogger(__name__)


def global_macro():
    return "global macro"


def setup(hass, config):
    _LOGGER.info("Setup custom macro")
    hass_tpl = Template("", hass)
    hass_tpl._env.globals['global_macro'] = global_macro

    return True
