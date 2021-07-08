# Check if pool pump is supposed to run, and turn it on or off accordingly
import logging

from datetime import timedelta

from homeassistant.helpers.sun import get_astral_event_date
from homeassistant.util import dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'pool_pump_service'

ATTRIBUTE_SWITCH_ENTITY_ID = 'switch_entity_id'
OFF_SEASON_MAX_DURATION = 6.0
OFF_SEASON_RUN_1_AFTER_SUNRISE_OFFSET_MINS = 120
OFF_SEASON_1ST_BREAK_MINUTES = 120
SWIMMING_SEASON_MAX_DURATION = 8.25
SWIMMING_SEASON_RUN_1_AFTER_SUNRISE_OFFSET_MINS = 120
SWIMMING_SEASON_BREAK_1_MINUTES = 180
SWIMMING_SEASON_BREAK_2_MINUTES = 180

def setup(hass, config):

    """Set up is called when Home Assistant is loading our component."""
    def switch_pool_pump(switch_entity_id, target_state):
        switch = hass.states.get(switch_entity_id)
        if switch:
            if switch.state == target_state:
                # Already in the correct state
                _LOGGER.info("Switch is in correct state: %s", target_state)
            else:
                # Not in the correct state
                data = { "entity_id": switch_entity_id }
                if target_state == 'on':
                    hass.services.call('switch', 'turn_on', data)
                else:
                    hass.services.call('switch', 'turn_off', data)
                _LOGGER.info("Switched from '%s' to '%s'", switch.state, target_state)
        else:
            _LOGGER.warning("Switch unavailable: %s", switch_entity_id)

    def handle_check(call):
        _LOGGER.info("Starting pool pump check")
        switch_entity_id = call.data.get(ATTRIBUTE_SWITCH_ENTITY_ID)
        # Read the pool pump configuration
        mode = hass.states.get('input_select.pool_pump')
        swimming_season = hass.states.get('input_boolean.swimming_season')

        run_hours_swimming_season = min(SWIMMING_SEASON_MAX_DURATION,
                                        float(hass.states.get(
                                              'input_number.run_pool_pump_hours_swimming_season').state))
        run_hours_off_season = min(OFF_SEASON_MAX_DURATION,
                                   float(hass.states.get(
                                         'input_number.run_pool_pump_hours_off_season').state))
        _LOGGER.info("* Pool pump mode: %s", mode.state)
        _LOGGER.info("* Swimming season: %s", swimming_season.state)
        _LOGGER.info("* Pool pump run hours swimming season: %s",
                     run_hours_swimming_season)
        _LOGGER.info("* Pool pump run hours off season: %s",
                     run_hours_off_season)
        # Only check if pool pump is set to 'Auto'
        if mode.state == 'Auto':
            _LOGGER.info("Pool pump set to 'Auto'")
            # Get sun details for today
            now = dt_util.now()
            _LOGGER.info("* Time is now %s", now)
            sun = hass.states.get('sun.sun')
            if sun.state == 'above_horizon':
                _LOGGER.info("* Sun above horizon")
                date = now.date()
                sunrise = get_astral_event_date(hass, 'sunrise', date)
                sunset = get_astral_event_date(hass, 'sunset', date)
                # _LOGGER.info("* Sunrise: %s",
                #              sunrise.astimezone(hass.config.time_zone))
                # _LOGGER.info("* Sunset: %s",
                #              sunset.astimezone(hass.config.time_zone))
                if swimming_season.state == 'on':
                    # Swimming Season (Summer)
                    _LOGGER.info("* Swimming season")
                    duration1 = run_hours_swimming_season * 60.0 * 0.25
                    duration2 = run_hours_swimming_season * 60.0 * 0.5
                    duration3 = run_hours_swimming_season * 60.0 * 0.25
                    _LOGGER.info(
                        "* Run pool pump 3 times for %s/%s/%s minutes",
                        duration1, duration2, duration3)
                   # Check for 1st run
                    run_1_start = sunrise + timedelta(
                        minutes=SWIMMING_SEASON_RUN_1_AFTER_SUNRISE_OFFSET_MINS)
                    run_1_stop = run_1_start + timedelta(minutes=duration1)
                    # _LOGGER.info("* Run 1/3: %s - %s",
                    #              run_1_start.astimezone(hass.config.time_zone),
                    #              run_1_stop.astimezone(hass.config.time_zone))
                    if run_1_start <= now <= run_1_stop:
                        # Turn on pool pump
                        _LOGGER.info("* Pool pump should be on (Run 1/3)")
                        switch_pool_pump(switch_entity_id, 'on')
                    else:
                        # Check for 2nd run
                        run_2_start = run_1_stop + timedelta(
                            minutes=SWIMMING_SEASON_BREAK_1_MINUTES)
                        run_2_stop = run_2_start + timedelta(minutes=duration2)
                        # _LOGGER.info("* Run 2/3: %s - %s",
                        #              run_2_start.astimezone(
                        #                  hass.config.time_zone),
                        #              run_2_stop.astimezone(
                        #                  hass.config.time_zone))
                        if run_2_start <= now <= run_2_stop:
                            # Turn on pool pump
                            _LOGGER.info("* Pool pump should be on (Run 2/3)")
                            switch_pool_pump(switch_entity_id, 'on')
                        else:
                            # Check for 3rd run
                            run_3_start = run_2_stop + timedelta(
                                minutes=SWIMMING_SEASON_BREAK_2_MINUTES)
                            run_3_stop = run_3_start + timedelta(
                                minutes=duration3)
                            # _LOGGER.info("* Run 3/3: %s - %s",
                            #              run_3_start.astimezone(
                            #                  hass.config.time_zone),
                            #              run_3_stop.astimezone(
                            #                  hass.config.time_zone))
                            if run_3_start <= now <= run_3_stop:
                                # Turn on pool pump
                                _LOGGER.info(
                                    "* Pool pump should be on (Run 3/3)")
                                switch_pool_pump(switch_entity_id, 'on')
                            else:
                                # Turn off pool pump
                                _LOGGER.info("* Pool pump should be off")
                                switch_pool_pump(switch_entity_id, 'off')
                else:
                    # Off Season (Winter)
                    _LOGGER.info("* Off season")
                    duration = run_hours_off_season * 60.0 * 0.5
                    _LOGGER.info("* Run pool pump 2 times for %s/%s minutes",
                                 duration, duration)
                    # Check for 1st run
                    run_1_start = sunrise + timedelta(
                        minutes=OFF_SEASON_RUN_1_AFTER_SUNRISE_OFFSET_MINS)
                    run_1_stop = run_1_start + timedelta(minutes=duration)
                    # _LOGGER.info("* Run 1/2: %s - %s",
                    #              run_1_start.astimezone(hass.config.time_zone),
                    #              run_1_stop.astimezone(hass.config.time_zone))
                    if run_1_start <= now <= run_1_stop:
                        # Turn on pool pump
                        _LOGGER.info("* Pool pump should be on (Run 1/2)")
                        switch_pool_pump(switch_entity_id, 'on')
                    else:
                        # Check for 2nd run
                        run_2_start = run_1_stop + timedelta(
                            minutes=OFF_SEASON_1ST_BREAK_MINUTES)
                        run_2_stop = run_2_start + timedelta(minutes=duration)
                        # _LOGGER.info("* Run 2/2: %s - %s",
                        #              run_2_start.astimezone(
                        #                  hass.config.time_zone),
                        #              run_2_stop.astimezone(
                        #                  hass.config.time_zone))
                        if run_2_start <= now <= run_2_stop:
                            # Turn on pool pump
                            _LOGGER.info("* Pool pump should be on (Run 2/2)")
                            switch_pool_pump(switch_entity_id, 'on')
                        else:
                            # Turn off pool pump
                            _LOGGER.info("* Pool pump should be off")
                            switch_pool_pump(switch_entity_id, 'off')
            else:
                _LOGGER.info("* Sun below horizon")
                # Turn pool pump if it's still running
                _LOGGER.info("* Pool pump should be off")
                switch_pool_pump(switch_entity_id, 'off')
        else:
            _LOGGER.info("Pool pump set to '%s'", mode.state)
    hass.services.register(DOMAIN, 'check', handle_check)
    # Return boolean to indicate that initialisation was successfully.
    return True
