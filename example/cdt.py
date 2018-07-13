import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rpyg import Rpyg

# ascii art from https://www.asciiart.eu/nature/mountains


def horizon():
    return '''
                      _                                                         
                     /#\                                                        
                    /###\     /\                                                
                   /  ###\   /##\  /\                                           
                  /      #\ /####\/##\                                          
                 /  /      /   # /  ##\             _       /\                  
               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\           
              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\          
             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\         
     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\     
  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \    
 /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /.. \    /...\ /  \ \   
/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \   
 .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\      
::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::..      
;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..   
;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;   

You are in the desert and are in need of shelter.
A stream winds [north] and mountains are visible to the [south].
What direction do you want to go? '''


def house():
    return '''
                                   /\                                          
                              /\  //\\                                      
                       /\    //\\///\\\        /\                           
                      //\\  ///\////\\\\  /\  //\\                          
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \                         
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \                        
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *               
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\              
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\             
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\            
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\           
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\          
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |              
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo       
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo                   

You are in front of a house! The door is locked [unlock_door]. To the       
[south] are mountains and to the [north] is more house.                     
What would you like to do?                                                  '''


def mountains():
    return '''
    .                  .-.    .  _   *     _   .                    
           *          /   \     ((       _/ \       *    .          
         _    .   .--'\/\_ \     `      /    \  *    ___            
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *         
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .       
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _        
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \       
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \      
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.    
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%  
@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%  
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::  
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'   
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'    

You are in the mountains. There is a key at your feet [pick_up_key].
To the [north] is a house to the [south] are more mountains.
What would you like to do?                                          '''


# https://www.asciiart.eu/nature/deserts
def desert():
    return '''
           ,                        '           .        '        ,     
   .            .        '       .         ,                            
                                                   .       '     +      
       +          .```````.                                             
                .'         `.   +     .     ________||                  
       ___     :             :     |       /        ||  .     '___      
  ____/   \   :               :   ||.    _/      || ||\_______/   \     
 /         \  :      _/|      :   `|| __/      ,.|| ||             \    
/  ,   '  . \  :   =/_/      :     |'_______     || ||  ||   .      \   
    |        \__`._/ |     .'   ___|        \__   \\||  ||...    ,   \  
   l|,   '   (   /  ,|...-'        \   '   ,     __\||_//___            
 ___|____     \_/^\/||__    ,    .  ,__             ||//    \    .  ,   
           _/~  `""~`"` \_           ''(       ....,||/       '         
 ..,...  __/  -'/  `-._ `\_\__        | \           ||  _______   .     
                '`  `\   \  \-.\        /(_1_,..      || /                
                                            ______/""""                 '''


# https://www.asciiart.eu/miscellaneous/keys
def key():
    return '''
  ooo,    .---.                 
 o`  o   /    |\________________    
o`   'oooo()  | ________   _   _)   
`oo   o` \    |/        | | | |     
  `ooo'   `---'         "-" |_|     
                                    
You have the key!                   '''


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
    'greeting': desert(),
    'name': 'Hiking the Continental Divide Trail!',
    'frames': {
        'entry': {
            'intro': horizon(),
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
            'intro': house(),
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
            'intro': 'You are inside the house! [celebrate]',
            'actions': {
                'celebrate': {
                    'frame': 'end',
                    'result': 'YAY its amazing!'
                }
            },
            'moves': {}
        },
        'mountains': {
            'intro': mountains(),
            'actions': {
                'pick_up_key': {
                    'frame': 'mountains_no_key',
                    'item': 'key',
                    'result': key()
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
