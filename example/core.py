import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rpg import Rpg

game = {
    'greeting': 'Welcome!',
    'name': 'Hiking the AT',
    'frames': {
        'entry': {
            'intro': 'A stream is to the north and mountains are on the horizon. What direction do you want to go? ',
            'actions': {
                'open_door': 'The door is locked',
                'unlock_door': ''
            },
            'moves': {
                'south': 'foothills',
                'north': 'dead_end'
            }
        },
        'dead_end': {
            'intro': 'You have reached a dead end',
            'actions': {
                'open_door': 'The door is locked',
                'unlock_door': ''
            },
            'moves': ''
        },
        'foothills': {
            'intro':
                '''The mountains are to the further to the south. A house is to the west. What direction do you want to go?
                ''',
            'actions': {
                'open_door': 'The door is locked',
                'unlock_door': ''
            },
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        },
        'house': {
            'intro': 'You are in front of a house! Where would you like to go?',
            'actions': {
                'open_door': 'The door is locked',
                'unlock_door': ''
            },
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        },
        'mountains': {
            'intro': 'You are in the mountains',
            'actions': {
                'open_door': 'The door is locked',
                'unlock_door': ''
            },
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        }
    }
}

if __name__ == '__main__':
    run = Rpg(**game)
    run.start()
