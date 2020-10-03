"""============================================================================

  Player space ship

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional

============================================================================"""
import pygame
from game_functions.gameobject import *
import config

fire_rate = 3

class BasicPlayer(Gameobject):
  # Variables to store animations and sounds common to all Player object
  loaded = False
  sprite = None

  # Initialize Player 
  def __init__(self, boundary = None, position = None, speed = 20):
    print("init Bacis Player")
    # Load animations and sounds first time this class is used
    if not BasicPlayer.loaded:
      BasicPlayer.size = (80,80)
      BasicPlayer.sprite = Animation("basic_player.png", (100,100), BasicPlayer.size,23) # sprite map
      BasicPlayer.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position, self.sprite.size, speed)

    # Set charakteristica other than default
    self.type = self.Type.PLAYER
    self.impact_power = 0

    # Make this object accessable to other objects
    self.game_state.player = self # !

    # Make sure position is within boundarys
    self.move()

  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    if scroll[0] or scroll[1]:
      self.boundary.move(scroll)
      self.rect.move(scroll)

    if not self.inactive:
      # Move player according to input
      if self.game_state.key['left']:
        self.direction = 180
        self.move()
      
      if self.game_state.key['right']:
        self.direction = 0
        self.move()
      
      if self.game_state.key['up']:
        self.direction = 90
        self.move()
      
      if self.game_state.key['down']:
        self.direction = 270
        self.move()
      

  # When hit or hitting something
  def hit(self, obj):
    if obj.type == self.Type.CGO or obj.type == self.Type.UNFREINDLY:
      print("I was hit by",obj.type,obj.__class__.__name__,obj.impact_power)
      self.health -= max( obj.impact_power + self.armor, 0)

    if self.health <= 0:
      # Reset player death animation
      self.sprite_dying.frame_time = False
      self.inactive = True
      #self.delete = True


