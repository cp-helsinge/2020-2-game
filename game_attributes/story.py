'''============================================================================

Story board

The story board is a list (Array) of levels. index is 0 - number of levels.

Each level consist of a list of game objects, that occur on that level. 
Including background, player, music etc. In short: all things that occur in 
that level of the game. 
It also might have a next_level object, that plays, when the level is 
successfully completed.

The game object list contains dictionaries (Associative arrays) That name and 
describe each game object, and its parameters.
Each game object has a member named 'class_name' all subsequent members are 
parameters, specific to that class.


============================================================================'''
#import sys
import pygame
#from pygame.locals import *

level = []

# Level 0 =====================================================================
# This level is not used. However the next_level effect will be played, before 
# the game begins.

level.append( [
  {
    'class_name': 'NextLevel',
    'sound'         : 'level2.ogg',
    'text'          : '<- -> or A D to move\n[Enter] [space] or mouse button right, to shoot',
    'intro_time'    : 2, 
    'intro_effect'  : 'slide_down', 
    'hold_time'     : 2, 
    'outtro_time'   : 1, 
    'outtro_effect' : 'slide_down'
  }
] )

# Level 1 =====================================================================
# Learn to play and feel a success
level.append([
  {'class_name': 'Background', 'color': pygame.Color('dodgerblue1')},
  {'class_name': 'Music', 'file name': 'theme1.ogg'},
  {'class_name': 'Player', 'position': (550,550), 'boundary': (0,000,1200,650)} 
])

# Level 2 =====================================================================
# devious deployment of aliens


# Level 3 =====================================================================
# devious deployment of aliens



