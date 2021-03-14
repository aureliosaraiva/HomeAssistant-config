# Check if pool pump is supposed to run, and turn it on or off accordingly
import logging

from datetime import timedelta

from homeassistant.util import dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'ct_light'

ATTRIBUTE_ENTITY_ID = 'entity_id'

def setup(hass, config):

    def handle_turn_on(call):
        _LOGGER.info("Starting turn_on TEST")
        entity_id = call.data.get(ATTRIBUTE_ENTITY_ID)
        circadian_values = hass.states.get('sensor.circadian_values')
        # colortemp = circadian_values['colortemp']
        # xy_color = circadian_values['xy_color']
        _LOGGER.info(circadian_values)
        _LOGGER.info(circadian_values.state)
        _LOGGER.info(circadian_values.colortemp)
        # _LOGGER.info(colortemp)
        # _LOGGER.info(xy_color)

    hass.services.register(DOMAIN, 'turn_on', handle_turn_on)
    # Return boolean to indicate that initialisation was successfully.
    return True
