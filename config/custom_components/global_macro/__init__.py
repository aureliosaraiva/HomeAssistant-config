import logging
import random
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.template import Template, is_template_string


_LOGGER = logging.getLogger(__name__)


DOMAIN = 'global_macro'
CONF_SPEECH = 'speech'


def setup(hass, config):
    _LOGGER.info("Setup global_macro")
    speech_category = dict()

    for n in config[DOMAIN]:
        speech = config[DOMAIN][n]
        for s in speech:
            speech_category[s] = speech[s]

    hass_tpl = Template("", hass)
    hass_tpl._env.globals['global_macro'] = _global_macro
    hass_tpl._env.globals['random_speech'] = _speech(speech_category)

    return True


def _speech(config):
    def _function(name):
        try:
            speechs = config.get(name)
            return random.choice(speechs)
        except:
            return 'Error'
    return _function


def _global_macro():
    return "global macro"
