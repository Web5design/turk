import string
import logging

# D-BUS services and interfaces
TURK_BRIDGE_SERVICE = "org.turkinnovations.turk.Bridge"
TURK_BRIDGE_INTERFACE = "org.turkinnovations.turk.Bridge"
TURK_DRIVER_INTERFACE = "org.turkinnovations.turk.Driver"
TURK_SPAWNER_SERVICE = "org.turkinnovations.turk.Spawner"
TURK_SPAWNER_INTERFACE = "org.turkinnovations.turk.Spawner"
TURK_DRIVER_ERROR = "org.turkinnovations.turk.DriverError"

# XMPP Namespace
TURK_XMPP_NAMESPACE = "http://turkinnovations.com/protocol"

# Default values for config (used when keys are left out)
DEFAULT = {
    'global': {
        'bus': 'SessionBus',
    },
    'turkctl': {
        'pidfile': '/etc/turk/turk.pid',
        'debug': True,
    },
    'bridge': {
        'server': 'macpro.local',
        'port': 5222,
        'username': 'platform@macpro.local',
        'password': 'password',
        'debug': True,
    },
    'spawner': {
        'autostart': [],
        'drivers': '/usr/share/turk/drivers',
        'debug': False,
    },
    'xbeed': {
        'name': 'xbee0',
        'port': '/dev/ttyUSB0',
        'baudrate': 9600,
        'escaping': True,
        'debug': True,
    }
}

def get_config(key, conf=DEFAULT):
    """
    Uses a dot-separated string to look up values from the configuration file.
    Falls back on the default values if not found.
    """
    temp = conf
    try:
        for query in key.split('.'):
            temp = temp.__getitem__(query)
        return temp
    except Exception, e:
        if conf != DEFAULT:
            return get_config(key)
        else:
            raise KeyError(key)

def get_configs(keys, conf=DEFAULT, prefix=''):
    all = []
    for key in keys:
        all.append(get_config('.'.join([prefix, key]), conf))
    return tuple(all)

def init_logging(module):
    logging.basicConfig(format = '(%(levelname)s) %(name)s: %(message)s')
    log = logging.getLogger(module)
    log.setLevel(logging.DEBUG)
    return log


