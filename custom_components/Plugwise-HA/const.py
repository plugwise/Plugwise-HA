"""Constant for Plugwise component."""

DOMAIN = "Plugwise-HA"


# Default directives
DEFAULT_NAME = "Plugwise"
DEFAULT_USERNAME = "smile"
DEFAULT_TIMEOUT = 10
DEFAULT_PORT = 80
DEFAULT_MIN_TEMP = 4
DEFAULT_MAX_TEMP = 30
DEFAULT_SCAN_INTERVAL = { 'thermostat': 60, 'power': 10 }

DEVICE_CLASS_GAS = "gas"

# Configuration directives
CONF_MIN_TEMP = "min_temp"
CONF_MAX_TEMP = "max_temp"
CONF_THERMOSTAT = "thermostat"
CONF_POWER = "power"
CONF_HEATER = "heater"
CONF_SOLAR = "solar"
CONF_GAS = "gas"

ATTR_ILLUMINANCE = "illuminance"

# Icons
THERMOSTAT_ICON = "mdi:thermometer"
WATER_HEATER_ICON = "mdi:thermometer"
GAS_ICON = "mdi:fire"
POWER_ICON = "mdi:flash"
POWER_FAILURE_ICON = "mdi:flash-off"
SWELL_SAG_ICON = "mdi:pulse"


