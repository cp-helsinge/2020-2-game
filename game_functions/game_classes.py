"""============================================================================

  Game classes 

============================================================================"""
# Import python modules
import pygame
from pygame.locals import *
import time
import os
import sys
import glob
import config
from game_functions import common

game_objects_from = 'game_objects' # Used to import game objects dynamically as the from part

class GameClasses:
  name_list = None
  def __init__(self):
    print("Loading game object classes...")
    # List of game object for current level
    self.list = []

    # Make list of file names in game objects
    if not GameClasses.name_list:
      GameClasses.name_list = {}
      for file in glob.glob(os.path.join(config.game_obj_path,"*.py")):
        # Extract the file name, without extension and in lower case 
        name = os.path.splitext(os.path.basename(file))[0]
        # Ignore private and protected files
        if name.startswith("_"): continue

        # Convert snake_name name to camelCase
        cc_name = common.sn2cc(name)

        # Import each file and itas primary class     
        if not cc_name in GameClasses.name_list:
          print("..loading",name +"."+cc_name)
          # from <game_objects_from> import <name>
          cls = __import__(game_objects_from, None, None, [name], 0)
          # class = <name>.<Name>
          GameClasses.name_list[cc_name] = getattr( getattr(cls,name), cc_name )

          #except Exception as err:
          #  print("Unable to load game object in", name + ".py", err)
      self.class_list = GameClasses.name_list    
      print(len(self.class_list)," Game Classes loaded.")

  # Add a game object to the running game
  def add(self, obj_description):  
    descr = obj_description.copy()
    name = descr['class_name']
    if not name in GameClasses.name_list:
      print("Error when adding game object: \""+ name + "\" is not a known object class name")
      print("-- Valid classes are:",*list(GameClasses.name_list.keys()), sep=", ")
      sys.exit(1) 

    del descr['class_name']

    # Create the new object and add it to the list
    #try:
    obj = GameClasses.name_list[name](**descr) 
    self.list.append(obj)
    #except Exception as err:
    #  print("Error when creating game object", name, " with parameters:", obj_description)
    #  print(err)
    #  sys.exit(1)  
