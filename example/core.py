import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import rpg

game = {
    'greeting': 'Welcome!',
    'name': 'Hiking the AT'
}

run = rpg.Rpg(**game)
