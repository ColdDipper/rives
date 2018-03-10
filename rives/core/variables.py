"""
This file is part of the "rives" project.
Please see the repository's LICENSE file for copying.
"""

from .text_styles import yellow, red, green, blue, white


RIVES_VERSION = '0.0.1'
RIVES_BANNER = '''\
     ____  _____   _____                                            _    
    |  _ \| ____| |  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
    | |_) |  _|   | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
    |  _ <| |___  |  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
    |_| \_\_____| |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\\

           [=[ Rives Exploitation Framework - {y}version:{g} {v_number:<5}{w} ]=]
           [=[     Type in "{r}help{w}" for a list of commands     ]=]
           [=[          {s:<2}Available exploits: {b}{n_exploits:<14}{w} ]=]
'''.format(y=yellow, b=blue, g=green, r=red, w=white, v_number=RIVES_VERSION, n_exploits=3, s='')
