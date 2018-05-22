import os
import sys
import unittest
# https://docs.python.org/3/library/unittest.html

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rpg import Rpg


hike = {
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
        }
    }
}


class TestGameMethods(unittest.TestCase):
    def setUp(self):
        self.game = Rpg(**hike)

    def test_init(self):
        self.assertEqual(self.game.name, hike['name'])


if __name__ == '__main__':
    unittest.main()