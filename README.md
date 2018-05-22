# python-console-game
Python port of console-game rpg engine

## Components

Each game will be an instance of the game engine initialzed with a game object 'cartridge'.

### Game Engine

Contains basic game elements:
- player
- player actions
- frames
- frame actions
- movement
- map
- rooms
- items

And user interface support elements
- inventory
- help
- input
- output


### Game Cartridge

Defines the game and an options object.

```
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
        }
    }
}
```


### Tests

```
python -m unittest
```


### References

(Python Unit Testing – Structuring Your Project)[http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/]