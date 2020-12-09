"""============================================================================

  Player 
  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional

============================================================================"""
import pygame
import numpy
from game_functions.gameobject import *
import config

fire_rate = 5

class Karlson(Gameobject):
  # Variables to store animations and sounds common to all Player object
  loaded = False
  sprite = None

  # Initialize Player 
  def __init__(self, boundary = None, position = None, speed = 20):
    
    # Load animations and sounds first time this class is used
    if not Karlson.loaded:
      print("Init", self.__class__.__name__)
      Karlson.size = (40,80)
      Karlson.sprite = Animation("karlson_hover50x100.png", (50,100), Karlson.size,7) # sprite map
      Karlson.sound_shoot = Sound("shot.ogg")
      Karlson.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position, self.sprite.size, speed)

    self.fire_rate = fire_rate
    self.last_shot = 0
    self.jumping = 0

    # Set charakteristica other than default
    self.type = self.Type.PLAYER
    self.impact_power = 100
    self.ampr = 1000

    # Make this object accessable to other objects
    self.game_state.player = self # !

    self.speed = [0,0]
    self.gravity = 5 
    self.jump_speed = 25
    

    # Make sure position is within boundarys
    self.move()

  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    if not self.inactive:
      # Move player according to input by adding speed, in one or more directions
      if self.game_state.key['left']:
        self.speed = [- 10,self.speed[1]]
      
      if self.game_state.key['right']:
        self.speed = [10,self.speed[1]]

      if self.game_state.key['jump'] and self.jumping < 1 and self.speed[1] == 0:
        self.jumping = 2
        self.speed = [self.speed[0], - self.jump_speed]

      # Fire, but only if  1 / fire_rate seconds has passed since last shot
      if self.game_state.key['fire'] and ( ( pygame.time.get_ticks() - self.last_shot ) > 1000 / self.fire_rate ):
        # Save stooting time
        self.sound_shoot.play()
        self.last_shot = pygame.time.get_ticks()
        start_position = self.rect.midleft if self.sprite.orientation != 0 else self.rect.midright
        start_position = [start_position[0],start_position[1]-12]
        direction = 180 if self.sprite.orientation != 0 else 0
        self.game_state.game_objects.add({
          'class_name': 'DiscoMamster',
          'position': start_position,
          'boundary': None,
          'speed': [10,0],
          'direction': direction
        })

      # Change orientation of animation to match movie direction
      if self.speed[0] > 0:
        self.sprite.orientation = 0
      elif self.speed[0] < 0:  
        self.sprite.orientation = 179 

      # Move animation
      self.speed = self.move(self.speed[0], self.speed[1])

      # Determin if still performing a jump
      if self.jumping > 0:
        if self.speed[1] < 0: # going up
          self.jumping = 2
        elif self.speed[1] == 0: 
          self.jumping -= 1 
        if self.jumping == 0:
          # if on the ground, set horisontal intertia is zero    
          self.speed[0] = 0

      if not self.jumping:
        self.speed[0] = 0

      # Add gravity
      self.speed = [self.speed[0],self.speed[1] + self.gravity]

  # When hit or hitting something
  def hit(self, obj):
    if obj.type == self.Type.CGO or obj.type == self.Type.UNFREINDLY:
      print("I was hit by",obj.type,obj.__class__.__name__,obj.impact_power)
      # self.health -= max( obj.impact_power + self.armor, 0)

    # prevent going through stationary objects 
    elif obj.type == self.Type.NEUTRAL:
      # stay on top or beside stationary object
      #print("I bumped into",obj.type,obj.__class__.__name__,obj.impact_power)
      self.uncollide_rect(obj.rect, self.gravity)
      self.speed = [0, 0]

    if self.health <= 0:
      # Reset player death animation
      self.inactive = True
      # self.delete = True
      print("You died")


