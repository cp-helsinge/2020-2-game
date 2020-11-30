"""============================================================================

  Player 
  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional

============================================================================"""
import pygame
from game_functions.gameobject import *
import config

fire_rate = 3

class Karlson(Gameobject):
  # Variables to store animations and sounds common to all Player object
  loaded = False
  sprite = None

  # Initialize Player 
  def __init__(self, boundary = None, position = None, speed = 20):
    print("init karlson")
    # Load animations and sounds first time this class is used
    if not Karlson.loaded:
      Karlson.size = (80,80)
      Karlson.sprite = Animation("karlson_hover100x100.png", (100,100), Karlson.size,7) # sprite map
      Karlson.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position, self.sprite.size, speed)

    # Set charakteristica other than default
    self.type = self.Type.PLAYER
    self.impact_power = 0

    # Make this object accessable to other objects
    self.game_state.player = self # !

    self.speed = [0,0]
    self.jumping = False
    self.gravity = 9.81 
    

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

    # Add gravity
    self.speed = [a+b for a,b in zip(self.speed,[0,self.gravity])]

    if not self.inactive:
      # Move player according to input. Add two lists using list comprehension ans zip (pair iterators)
      if self.game_state.key['left']:
        self.speed = [a+b for a,b in zip(self.speed,[-10,0])]
      
      if self.game_state.key['right']:
        self.speed = [a+b for a,b in zip(self.speed,[10,0])]

      if not self.jumping and self.game_state.key['jump']:
        self.jumping = True
        self.speed = [a+b for a,b in zip(self.speed,[0,-100])]
        print("Jumping")

      self.speed = self.move(self.speed[0], self.speed[1])

      if self.jumping and self.speed[0] == 0:
        self.jumping = False

  # When hit or hitting something
  def hit(self, obj):
    if obj.type == self.Type.CGO or obj.type == self.Type.UNFREINDLY:
      print("I was hit by",obj.type,obj.__class__.__name__,obj.impact_power)
      self.health -= max( obj.impact_power + self.armor, 0)

    # prevent going through stationary objects 
    elif obj.type == self.Type.NEUTRAL:
      pass
      # if self.touch(obj.rect, self.rect):
        # stay on top or beside stationary object
        

    if self.health <= 0:
      # Reset player death animation
      self.sprite_dying.frame_time = False
      self.inactive = True
      #self.delete = True


