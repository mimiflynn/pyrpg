import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import rpg

game = {
    'greeting': 'Welcome!',
    'name': 'Hiking the AT',
    'frames': {
        'entry': {
            'intro': 'A stream is to the north and mountains are on the horizon. What direction do you want to go? ',
            'moves': {
                'south': 'foothills',
                'north': 'dead_end'
            }
        },
        'dead_end': {
            'intro': 'You have reached a dead end',
            'moves': '',
        },
        'foothills': {
            'intro':
                '''The mountains are to the further to the south. A house is to the west. What direction do you want to go?
                ''',
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        },
        'house': {
            'intro': 'You are in a house!',
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        },
        'mountains': {
            'intro': 'You are in the mountains',
            'moves': {
                'south': 'mountains',
                'west': 'house'
            }
        }
    }
}

run = rpg.Rpg(**game)
