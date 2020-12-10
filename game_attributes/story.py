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
  #{'class_name': 'Mars', 'position': (1,1)}

  # floor
  {'class_name': 'Brickwork', 'position':     (   0,635)},
  {'class_name': 'Brickwork', 'position':     (  50,635)},
  {'class_name': 'Brickwork', 'position':     ( 100,635)},
  {'class_name': 'BrickworkWorm', 'position': ( 150,635)},
  {'class_name': 'Brickwork', 'position':     ( 200,635)},
  {'class_name': 'Brickwork', 'position':     ( 250,635)},
  {'class_name': 'Brickwork', 'position':     ( 300,635)},
  {'class_name': 'Brickwork', 'position':     ( 350,635)},
  {'class_name': 'Brickwork', 'position':     ( 400,635)},
  {'class_name': 'Brickwork', 'position':     ( 450,635)},
  {'class_name': 'Brickwork', 'position':     ( 500,635)},
  #{'class_name': 'Brickwork', 'position':     ( 550,635)},
  {'class_name': 'LavaJuice', 'position':     ( 550,635)},
  {'class_name': 'LavaJuice', 'position':     ( 600,635)},
  #{'class_name': 'Brickwork', 'position':     ( 600,635)},
  {'class_name': 'Brickwork', 'position':     ( 650,635)},
  {'class_name': 'Brickwork', 'position':     ( 700,635)},
  {'class_name': 'Brickwork', 'position':     ( 750,635)},  
  {'class_name': 'Brickwork', 'position':     ( 800,635)},
  {'class_name': 'Brickwork', 'position':     ( 850,635)},
  {'class_name': 'Brickwork', 'position':     ( 900,635)},
  {'class_name': 'Brickwork', 'position':     ( 950,635)},
  {'class_name': 'Brickwork', 'position':     (1000,635)},
  {'class_name': 'Brickwork', 'position':     (1050,635)},
  {'class_name': 'Brickwork', 'position':     (1100,635)},
  {'class_name': 'Brickwork', 'position':     (1150,635)},

  # Stairs
  {'class_name': 'Brickwork', 'position':     ( 1150,535)},
  
  # legde 1
  {'class_name': 'Brickwork', 'position':     (   0,435)},
  {'class_name': 'Brickwork', 'position':     (  50,435)},
  {'class_name': 'Brickwork', 'position':     ( 100,435)},
  {'class_name': 'BrickworkWorm', 'position': ( 150,435)},
  {'class_name': 'Brickwork', 'position':     ( 200,435)},
  {'class_name': 'Brickwork', 'position':     ( 250,435)},
  {'class_name': 'Brickwork', 'position':     ( 300,435)},
  {'class_name': 'Brickwork', 'position':     ( 350,435)},
  {'class_name': 'Brickwork', 'position':     ( 400,435)},
  {'class_name': 'Brickwork', 'position':     ( 450,435)},
  {'class_name': 'Brickwork', 'position':     ( 500,435)},
  #{'class_name': 'Brickwork', 'position':     ( 550,435)},
  #{'class_name': 'Brickwork', 'position':     ( 600,435)},
  {'class_name': 'Brickwork', 'position':     ( 650,435)},
  {'class_name': 'Brickwork', 'position':     ( 700,435)},
  {'class_name': 'Brickwork', 'position':     ( 750,435)},  
  {'class_name': 'Brickwork', 'position':     ( 800,435)},
  {'class_name': 'Brickwork', 'position':     ( 850,435)},
  {'class_name': 'Brickwork', 'position':     ( 900,435)},
  {'class_name': 'Brickwork', 'position':     ( 950,435)},
  {'class_name': 'Brickwork', 'position':     (1000,435)},
  #{'class_name': 'Brickwork', 'position':     (1050,435)},
  #{'class_name': 'Brickwork', 'position':     (1100,435)},
  #{'class_name': 'Brickwork', 'position':     (1150,435)},

  # Stairs
  {'class_name': 'Brickwork', 'position':     (    0,335)},
  {'class_name': 'Brickwork', 'position':     (   50,385)},

  # legde 2
  #{'class_name': 'Brickwork', 'position':     (   0,235)},
  {'class_name': 'Brickwork', 'position':     (  50,235)},
  {'class_name': 'Brickwork', 'position':     ( 100,235)},
  {'class_name': 'BrickworkWorm', 'position': ( 150,235)},
  {'class_name': 'Brickwork', 'position':     ( 200,235)},
  {'class_name': 'Brickwork', 'position':     ( 250,235)},
  {'class_name': 'Brickwork', 'position':     ( 300,235)},
  {'class_name': 'Brickwork', 'position':     ( 350,235)},
  {'class_name': 'Brickwork', 'position':     ( 400,235)},
  {'class_name': 'Brickwork', 'position':     ( 450,235)},
  {'class_name': 'Brickwork', 'position':     ( 500,235)},
  {'class_name': 'Brickwork', 'position':     ( 550,235)},
  {'class_name': 'Brickwork', 'position':     ( 600,235)},
  {'class_name': 'Brickwork', 'position':     ( 650,235)},
  {'class_name': 'Brickwork', 'position':     ( 700,235)},
  {'class_name': 'Brickwork', 'position':     ( 750,235)},  
  {'class_name': 'Brickwork', 'position':     ( 800,235)},
  {'class_name': 'Brickwork', 'position':     ( 850,235)},
  {'class_name': 'Brickwork', 'position':     ( 900,235)},
  {'class_name': 'Brickwork', 'position':     ( 950,235)},
  {'class_name': 'Brickwork', 'position':     (1000,235)},
  {'class_name': 'Brickwork', 'position':     (1050,235)},
  {'class_name': 'Brickwork', 'position':     (1100,235)},
  {'class_name': 'Brickwork', 'position':     (1150,235)},

  # legde 3
  #{'class_name': 'Brickwork', 'position':     (   0,135)},
  #{'class_name': 'Brickwork', 'position':     (  50,135)},
  {'class_name': 'Brickwork', 'position':     ( 100,135)},
  {'class_name': 'BrickworkWorm', 'position': ( 150,135)},
  {'class_name': 'Brickwork', 'position':     ( 200,135)},
  {'class_name': 'Brickwork', 'position':     ( 250,135)},
  {'class_name': 'Brickwork', 'position':     ( 300,135)},
  {'class_name': 'Brickwork', 'position':     ( 350,135)},
  {'class_name': 'Brickwork', 'position':     ( 400,135)},
  {'class_name': 'Brickwork', 'position':     ( 450,135)},
  {'class_name': 'Brickwork', 'position':     ( 500,135)},
  {'class_name': 'Brickwork', 'position':     ( 550,135)},
  {'class_name': 'Brickwork', 'position':     ( 600,135)},
  {'class_name': 'Brickwork', 'position':     ( 650,135)},
  {'class_name': 'Brickwork', 'position':     ( 700,135)},
  {'class_name': 'Brickwork', 'position':     ( 750,135)},  
  {'class_name': 'Brickwork', 'position':     ( 800,135)},
  {'class_name': 'Brickwork', 'position':     ( 850,135)},
  {'class_name': 'Brickwork', 'position':     ( 900,135)},
  {'class_name': 'Brickwork', 'position':     ( 950,135)},
  {'class_name': 'Brickwork', 'position':     (1000,135)},
  {'class_name': 'Brickwork', 'position':     (1050,135)},
  #{'class_name': 'Brickwork', 'position':     (1100,135)},
  #{'class_name': 'Brickwork', 'position':     (1150,135)},

  {'class_name': 'Karlson', 'position': (40,650), 'boundary': (0,000,1200,650)},
  {'class_name': 'Kartoffel', 'position': (100,40)}, # denne er lavet af Snorre og skal pilles lidt i før den virker
  {'class_name': 'Pizza', 'position': (1000,185)},
  {'class_name': 'Marsmand', 'position': (350,350)},

])

# Level 2 =====================================================================
# deployment of primitive aliens


# Level 3 =====================================================================
# devious deployment of evil aliens


# Level 3 =====================================================================
# devious deployment of so many evil aliens the player will eventually die!
# (MUEHAHAHAHAHAAAAAAAARH!)



