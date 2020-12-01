"""============================================================================

  Basic Shot 

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
from game_functions.gameobject import *

class DiscoMamster(Gameobject):
  # Variables to store animations and sounds common to all Shot object
  loaded = False
  sprite = None
  sprit_bomb = None
  sprit_shot = None
  sound_die = None
  sound_shoot = None
  count = 0

  # Initialize Shot 
  def __init__(self, boundary = None, position = None, direction = 90, speed = 0):
    # Load animations and sounds first time this class is used
    if not DiscoMamster.loaded:
      DiscoMamster.sprite = Animation("disco_mamster.png",(20,20),(20,20)) 
      DiscoMamster.loaded = True # Indicate that all common external attributes are loaded
      DiscoMamster.count += 1

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position,self.sprite.size, speed, direction)
    
    # Adjust position to be centered on top of position
    if position:
      self.rect.center = position

    # Set charakteristica other than default
    self.type = self.Type.FREINDLY
    self.impact_power = 10
    self.health = 1

  def __del__(self):
    DiscoMamster.count -= 1

  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(DiscoMamster.count),self.rect)
    
  # Movement
  def update(self, scroll):
    x,y = self.move(self.speed,0)

    # test if out of boundary and deflect sprite by mirroring direction
    if x != self.speed:
      self.delete = True

  # When hit or hitting something
  def hit(self, obj):
    print(self.__class__.__name__,"hitting",obj.type,obj.__class__.__name__,obj.impact_power)
    if not obj.type == self.Type.PLAYER and not obj.type == self.Type.FREINDLY:
      self.delete = True