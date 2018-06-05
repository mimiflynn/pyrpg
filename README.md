# pyrpg
Python port of console-game rpg engine

## Components

Each game will be an instance of the game engine initialzed with a game object 'cartridge'.

### Game Engine

Create a new game:

```
from rpg import Rpg

run_game = Rpg(game)
run_game.start()
```

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

#### Game Object

`greeting` - string

`name` - string

`frames` - collection of frame objects

#### Frame Object

`intro` - string

`actions` - collection of action objects

`moves` - collection of move objects

`end` - boolean - indicates that this frame is the end of the game

#### Action Object

`result` - string - success message

`required` - string - item name - item required to be in user inventory to fulfill action. If the user does not have this item, a message will be displayed.

`frame` - string - frame name - destination that a successful action will advance to

#### Example Game
```
game = {
    'greeting': 'Welcome!',
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
                'south': 'foothills',
                'north': 'dead_end'
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
            'actions': {},
            'moves': {
                'south': 'dead_end',
                'north': 'house'
            }
        },
        'end': {
            'end': True
        }
    }
}
```

### Example Game
From project root:

```
python3 example/at.py
```


### Tests

```
python -m unittest
```


### References

[Python Unit Testing – Structuring Your Project](http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/)

[Text to ASCII Art Generator](http://patorjk.com/software/taag/)

[Modules and Packages](https://www.learnpython.org/en/Modules_and_Packages)

[setup.py](https://github.com/kennethreitz/setup.py)
