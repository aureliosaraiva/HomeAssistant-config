import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.components.light import LightEntity
from homeassistant.const import CONF_NAME, CONF_PLATFORM, STATE_ON
from homeassistant.util import slugify

from homeassistant.components.light import (
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    SUPPORT_COLOR_TEMP
)

from .const import (
    ICON,
    CURRENT_LIGHT_RGB,
    CURRENT_LIGHT_CT,
    CONF_LIGHTS_CT,
    CONF_LIGHTS_RGB,
    PLATFORM_NAME
)


_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = vol.Schema({
    vol.Required(CONF_PLATFORM): PLATFORM_NAME,
    vol.Optional(CONF_NAME, default="Merge Lighting"): cv.string,
    vol.Optional(CONF_LIGHTS_CT): cv.entity_id,
    vol.Optional(CONF_LIGHTS_RGB): cv.entity_id
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Merge Light."""
    _LOGGER.info("Setup platform")
    lights_ct = config.get(CONF_LIGHTS_CT)
    lights_rgb = config.get(CONF_LIGHTS_RGB)
    name = config.get(CONF_NAME)

    light_merge = LightMerge(hass, name, lights_ct, lights_rgb)
    add_devices([light_merge])

    return True


class LightMerge(LightEntity, RestoreEntity):
    """Representation of a Merge Light."""
    def __init__(self, hass, name, lights_ct, lights_rgb):
        """Initialize the Merge Light."""
        entity_name = slugify("{} {}".format(PLATFORM_NAME, name))
        self.hass = hass
        self._name = name
        self._entity_id = "light." + entity_name
        self._state = None
        self._icon = ICON
        self._hs_color = None
        self._brightness = None
        self._color_temp = None
        self._current_light = None

        self._lights_ct = lights_ct
        self._lights_rgb = lights_rgb

        self._supported_features = SUPPORT_COLOR
        self._supported_features |= SUPPORT_BRIGHTNESS
        self._supported_features |= SUPPORT_COLOR_TEMP

    def turn_on(self, **kwargs):
        """Turn on device."""
        if 'color_temp' in kwargs:
            self._color_temp = kwargs['color_temp']
            self._current_light = CURRENT_LIGHT_CT

        if 'hs_color' in kwargs:
            self._hs_color = kwargs['hs_color']
            self._current_light = CURRENT_LIGHT_RGB

        if 'brightness' in kwargs:
            self._brightness = kwargs['brightness']

        self._state = True
        self._update_state()

    def turn_off(self):
        """Turn off device."""
        self._state = False
        self._update_state()

    async def async_added_to_hass(self):
        """Call when entity about to be added to hass."""
        _LOGGER.info('async_added_to_hass')

        await super().async_added_to_hass()
        if self._state is not None:
            return

        state = await self.async_get_last_state()

        self._update_light(state)
        # self.update_light()
        self._state = state and state.state == STATE_ON

    @property
    def supported_features(self):
        """Flag supported features."""
        return self._supported_features

    @property
    def entity_id(self):
        """Return device entity id."""
        return self._entity_id

    @property
    def name(self):
        """Return device name."""
        return self._name

    @property
    def is_on(self):
        """Return device state on/off."""
        return self._state

    @property
    def icon(self):
        """Return device icon."""
        return self._icon

    @property
    def hs_color(self):
        """Return device hs color."""
        return self._hs_color

    @property
    def brightness(self):
        """Return device brightness."""
        return self._brightness

    @property
    def color_temp(self):
        """Return device color temp."""
        return self._color_temp

    @property
    def device_state_attributes(self):
        """Return device attributes."""
        data = {
            'color_temp': self.color_temp,
            'hs_color': self.hs_color,
            'brightness': self.brightness,
            'lights_ct': self._lights_ct,
            'lights_rgb': self._lights_rgb,
            'current_light': self._current_light
        }
        return data

    def _update_light(self, state):
        """Update device state."""
        if not state:
            return None

        properties = state.as_dict()
        attributes = properties['attributes']

        if 'hs_color' in attributes:
            self._hs_color = attributes['hs_color']

        if 'brightness' in attributes:
            self._brightness = attributes['brightness']

        if 'color_temp' in attributes:
            self._color_temp = attributes['color_temp']

        if 'current_light' in attributes:
            self._current_light = attributes['current_light']

    def _update_state(self):
        """Update device state."""
        hass = self.hass

        if not self._state:
            data = {"entity_id": [self._lights_rgb, self._lights_ct]}
            hass.services.call('light', 'turn_off', data)

        else:
            if self._current_light == CURRENT_LIGHT_CT:
                data = {'entity_id': self._lights_rgb}
                hass.services.call('light', 'turn_off', data)
                hass.services.call('light', 'turn_on', {
                    'entity_id': self._lights_ct,
                    'color_temp': self._color_temp,
                    'brightness': self._brightness
                })
            elif self._current_light == CURRENT_LIGHT_RGB:
                data = {'entity_id': self._lights_ct}
                hass.services.call('light', 'turn_off', data)
                hass.services.call('light', 'turn_on', {
                    'entity_id': self._lights_rgb,
                    'hs_color': self._hs_color,
                    'brightness': self._brightness
                })
            self.schedule_update_ha_state()
