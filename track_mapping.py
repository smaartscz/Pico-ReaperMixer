"""
TRACK MAPPING:
It's list with dictionary inside. Add new value at end of previous dictionary.

TEMPLATE:
    {"name": "Main", # Your name for use inside python
     "reaper": "Main", # Track name inside Reaper DAW
     "tracknumber": 0, # Leave default(It will be assaigned based on data from Reaper DAW)
     "slider": "1", # Must be higher than previous value for slider(simply add 1)
     "slider_value": 0.0, # Leave default(It will be assaigned based on data from HW pin)
     "slider_previous" : 0.0, # Leave default(It will be assaigned based on data from HW pin)
     "mute": "1", # Must be higher than previous value for mute(simply add 1)
     "mute_value": False, # Leave default(It will be assaigned based on data from HW pin)
     "mute_previous": False # Leave default(It will be assaigned based on data from HW pin)
     }
"""
mapping = [
    {"name": "Direct monitoring",
     "reaper": "Direct monitor",
     "tracknumber": 0,
     "slider": "1",
     "slider_value": 0.0,
     "slider_previous" : 0.0,
     "mute": "1",
     "mute_value": False,
     "mute_previous": False
     },
    {"name": "Main",
     "reaper": "Main",
     "tracknumber": 0,
     "slider": "2",
     "slider_value": 0.0,
     "slider_previous" : 0.0,     
     "mute": "2",
     "mute_value": False,
     "mute_previous": False
     },
    {"name": "Multimedia",
     "reaper": "Multimedia",
     "tracknumber": 0,
     "slider": "3",
     "slider_value": 0.0,
     "slider_previous" : 0.0,
     "mute": "3",
     "mute_value": False,
     "mute_previous": False
     },
    {"name": "Discord",
     "reaper": "Main",
     "tracknumber": 0,
     "slider": "4",
     "slider_value": 0.0,
     "slider_previous" : 0.0,
     "mute": "4",
     "mute_value": False,
     "mute_previous": False
     }          
]
