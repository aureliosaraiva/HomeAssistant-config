DEPENDENCIES = ['light']

import logging

from custom_components.circadian_lighting import DOMAIN, CIRCADIAN_LIGHTING_UPDATE_TOPIC, DATA_CIRCADIAN_LIGHTING

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.dispatcher import dispatcher_connect
from homeassistant.helpers.event import track_state_change
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.components.light import (
    is_on, ATTR_BRIGHTNESS, ATTR_COLOR_TEMP, ATTR_RGB_COLOR, ATTR_TRANSITION,
    VALID_TRANSITION, ATTR_WHITE_VALUE, ATTR_XY_COLOR, DOMAIN as LIGHT_DOMAIN)

from homeassistant.components.light import LightEntity

from homeassistant.const import (
    ATTR_ENTITY_ID, CONF_NAME, CONF_PLATFORM, STATE_ON,
    SERVICE_TURN_ON)
from homeassistant.util import slugify
from homeassistant.util.color import (
    color_RGB_to_xy, color_temperature_kelvin_to_mired,
    color_temperature_to_rgb, color_xy_to_hs)

_LOGGER = logging.getLogger(__name__)

ICON = 'mdi:theme-light-dark'

CONF_LIGHTS_CT = 'lights_ct'
CONF_LIGHTS_RGB = 'lights_rgb'


PLATFORM_SCHEMA = vol.Schema({
    vol.Required(CONF_PLATFORM): 'merge_light',
    vol.Optional(CONF_NAME, default="Merge Lighting"): cv.string,
    vol.Optional(CONF_LIGHTS_CT): cv.entity_ids,
    vol.Optional(CONF_LIGHTS_RGB): cv.entity_ids,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    lights_ct = config.get(CONF_LIGHTS_CT)
    lights_rgb = config.get(CONF_LIGHTS_RGB)

    cs = LightMerge(hass, cl, name, lights_ct, lights_rgb)
    add_devices([cs])

    # def update(call=None):
    #     """Update lights."""
    #     cs.update_switch()
    return True


class LightMerge(SwitchEntity, RestoreEntity):
    """Representation of a Circadian Lighting switch."""

    def __init__(self, hass, cl, name, lights_ct, lights_rgb, lights_xy, lights_brightness,
                    disable_brightness_adjust, min_brightness, max_brightness,
                    sleep_entity, sleep_state, sleep_colortemp, sleep_brightness,
                    disable_entity, disable_state, initial_transition):
        """Initialize the Circadian Lighting switch."""
        self.hass = hass
        self._cl = cl
        self._name = name
        self._entity_id = "light." + slugify("{} {}".format('light_merge', name))
        self._state = None
        self._icon = ICON

        self._lights_ct = lights_ct
        self._lights_rgb = lights_rgb

        self._lights = []
        if lights_ct != None:
            self._lights += lights_ct
        if lights_rgb != None:
            self._lights += lights_rgb

        """Register callbacks."""
        dispatcher_connect(hass, CIRCADIAN_LIGHTING_UPDATE_TOPIC, self.update_switch)
        track_state_change(hass, self._lights, self.light_state_changed)
        if self._sleep_entity is not None:
            track_state_change(hass, self._sleep_entity, self.sleep_state_changed)
        if self._disable_entity is not None:
            track_state_change(hass, self._disable_entity, self.disable_state_changed)

    @property
    def entity_id(self):
        """Return the entity ID of the switch."""
        return self._entity_id

    @property
    def name(self):
        """Return the name of the device if any."""
        return self._name

    @property
    def is_on(self):
        """Return true if circadian lighting is on."""
        return self._state

    async def async_added_to_hass(self):
        """Call when entity about to be added to hass."""
        # If not None, we got an initial value.
        await super().async_added_to_hass()
        if self._state is not None:
            return

        state = await self.async_get_last_state()
        self._state = state and state.state == STATE_ON

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def hs_color(self):
        return self._hs_color

    @property
    def device_state_attributes(self):
        """Return the attributes of the switch."""
        return self._attributes

    def turn_on(self, **kwargs):
        """Turn on circadian lighting."""
        self._state = True

        # Make initial update
        self.update_switch(self._initial_transition)

        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn off circadian lighting."""
        self._state = False
        self.schedule_update_ha_state()
        self._hs_color = None
        self._attributes['hs_color'] = self._hs_color
        self._attributes['brightness'] = None
