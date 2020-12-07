'''============================================================================

Story board

The story board is a list (Array) of levels. (Index 1 = first playable level)

Each level consist of a list of game objects, that occur on that level. 
Including background, player, music etc. In short: all things that occur in 
that level of the game. 
It might also include a next_level object, that plays, when the level is 
successfully completed.

The game object list contains dictionaries (Associative arrays) of maned parameters.
This dictionary must contain a 'class_name' that name the class to load.
All other entries are treated as parameters to the class.

ex:
  a play object, that occur at position y=550,y=500

  {
    'class_name': 'Player', 
    'position': (550,550), 
    'boundary': (0,000,1200,650)
  },

  an alien oponent class, appering 30 secons into the level:

  {
    'class_name': 'Alien',
    'delay': 30, 
    'position': (700,30), 
    'boundary': (0,0,1000,300), 
    'speed': 5,
    'direction': 20
  }
  
Class names are CamelCase with first letter as capital.

Special class_names are:
  Background 
  NextLevel
  Music
============================================================================

Internal documentation for Killer Potatoes:
player class = karlson.png
enemy class = AlienAlvin1

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
  {'class_name': 'Background', 'file_name': 'mars_1200x700.png','color': pygame.Color('dodgerblue1')},
  #{'class_name': 'Music', 'file name': 'theme1.ogg'},
  #{'class_name': 'BasicPlayer', 'position': (550,550), 'boundary': (0,000,1200,650)}, # dette er trekant-spille-figuren som vi har fjernet
  # {'class_name': 'BasicObject', 'position': (250,250)}, # dette er den grøne kasse som vi har fjernet
  {'class_name': 'Karlson', 'position': (550,250), 'boundary': (0,000,1200,650)},
  {'class_name': 'Kartoffel', 'position': (100,100)}, # denne er lavet af Snorre og skal pilles lidt i før den virker
  {'class_name': 'Pizza', 'position': (1000,340)},
  {'class_name': 'BrickTile', 'position': (0,650)},
  {'class_name': 'BrickTile', 'position': (1100,650)},
  {'class_name': 'Marsmand', 'position': (700,500)},
  #{'class_name': 'Mars', 'position': (1,1)}
])

# Level 2 =====================================================================
# deployment of primitive aliens


# Level 3 =====================================================================
# devious deployment of evil aliens


# Level 3 =====================================================================
# devious deployment of so many evil aliens the player will eventually die!
# (MUEHAHAHAHAHAAAAAAAARH!)



