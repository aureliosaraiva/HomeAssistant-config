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
    speaker = dict()

    _LOGGER.info(config[DOMAIN])

    for n in config[DOMAIN]:
        if n == 'speech':
            speech = config[DOMAIN][n]
            for s in speech:
                speech_category[s] = speech[s]
        else:
            sp = config[DOMAIN][n]
            for s in sp:
                speaker[s] = sp[s]

    _LOGGER.info(speaker)
    hass_tpl = Template("", hass)
    hass_tpl._env.globals['global_macro'] = _global_macro
    hass_tpl._env.globals['random_speech'] = _speech(speech_category)
    hass_tpl._env.globals['speaker'] = _speaker(speaker)


    return True

def _speaker(speaker):
    def _function(name):
        try:
            if name in speaker:
                return speaker[name]
            else:
                return speaker['default']
        except:
            return 'Error'
    return _function


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
