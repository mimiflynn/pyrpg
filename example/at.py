import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rpyg import Rpyg


def greeting():
    return '''
         _   _ _ _    _               _   _             ___ _____ 
        | | | (_) |  (_)             | | | |           / _ \_   _|
        | |_| |_| | ___ _ __   __ _  | |_| |__   ___  / /_\ \| |  
        |  _  | | |/ / | '_ \ / _` | | __| '_ \ / _ \ |  _  || |  
        | | | | |   <| | | | | (_| | | |_| | | |  __/ | | | || |  
        \_| |_/_|_|\_\_|_| |_|\__, |  \__|_| |_|\___| \_| |_/\_/  
                               __/ |                              
                              |___/                               '''


def win():
    return '''
         _____      _      _               _       
        /  __ \    | |    | |             | |      
        | /  \/ ___| | ___| |__  _ __ __ _| |_ ___ 
        | |    / _ \ |/ _ \ '_ \| '__/ _` | __/ _ |
        | \__/\  __/ |  __/ |_) | | | (_| | ||  __/
         \____/\___|_|\___|_.__/|_|  \__,_|\__\___|
                                                   
                                                   '''


game = {
    'greeting': greeting(),
    'name': 'Hiking the AT',
    'frames': {
        'entry': {
            'intro': 'A stream is to the north and mountains are on the horizon. What direction do you want to go? ',
            'actions': {
                'open_door': {
                    'result': 'The door is locked'
                },
                'unlock_door': {
                    'result': 'The door is locked'
                }
            },
            'moves': {
                'south': 'mountains',
                'north': 'house'
            }
        },
        'dead_end': {
            'intro': 'You have reached a dead end',
            'actions': {
                'open_door': {
                    'result': 'The door is locked'
                },
                'unlock_door': {
                    'result': 'The door is locked'
                }
            },
            'moves': {
                'south': 'mountains',
                'north': 'house'
            }
        },
        'house': {
            'intro': 'You are in front of a house! Where would you like to go?',
            'actions': {
                'unlock_door': {
                    'frame': 'inside_house',
                    'required': 'key',
                    'result': 'You have unlocked the door!'
                }
            },
            'moves': {
                'south': 'mountains',
                'north': 'house'
            }
        },
        'inside_house': {
            'intro': 'You are inside the house!',
            'actions': {
                'celebrate': {
                    'frame': 'end',
                    'result': 'YAY its amazing!'
                }
            },
            'moves': {}
        },
        'mountains': {
            'intro': 'You are in the mountains. There is a key at your feet.',
            'actions': {
                'pick_up_key': {
                    'frame': 'mountains_no_key',
                    'item': 'key',
                    'result': 'You have the key!'
                }
            },
            'moves': {
                'south': 'dead_end',
                'north': 'house'
            }
        },
        'mountains_no_key': {
            'intro': 'You are in the mountains.',
            'moves': {
                'south': 'dead_end',
                'north': 'house'
            }
        },
        'end': {
            'intro': win(),
            'end': True
        }
    }
}

run = Rpyg(**game)
run.start()
