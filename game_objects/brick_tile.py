"""============================================================================

  Basic game object

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
import math
from game_functions.gameobject import *

class BrickTile(Gameobject):
  # Variables to store animations and sounds common to all AlienAlvin1 object
  loaded = False
  sprite = None

  # === Initialize AlienAlvin1 ===
  def __init__(self, boundary = None, position = None, direction = 0, speed = 0, delay = 0):
    print("Init", self.__class__.__name__)
    
    # Load animations and sounds first time this class is used
    if not BrickTile.loaded:
      # Run this the first time this class is used
      BrickTile.size = (100,100)
      BrickTile.sprite = self.Animation("brick_tile100x100.png", (100,100), BrickTile.size,7) # Load sprite map
      BrickTile.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position, self.sprite.size, speed, direction)

    # Set charakteristica other than default
    self.type = self.Type.NEUTRAL # Type of object:   NEUTRAL, CGO, UNFREINDLY,  PLAYER, FREINDLY, PLAYER_OPPONENT

    # Delayed deployment
    self.delay = delay
    self.inactive = self.invisible = delay > 0
    self.move()
    

  # === Movement ===
  def update(self, scroll):
    self.move()
    pass

  # === Draw on game surface ===
  def draw(self, surface):
    if self.invisible:
      return

    # Flip image when direction is left
    surface.blit(self.sprite.get_surface(0),self.rect)


  # === When hit or hitting something ===
  def hit(self, obj):
    pass
