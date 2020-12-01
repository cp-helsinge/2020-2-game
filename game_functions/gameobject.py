"""============================================================================

  Game object template

  Inherited by all game objects

============================================================================"""
import pygame
import math
import random
import os
from game_functions.object_types import *
from game_functions.animation import *
from game_functions.audio import *
import config

class Gameobject(Animation, Sound):
  class Type(ObjectType):
    pass

  Animation = Animation

  def __init__(self, boundary = None, position=None, size=None, speed=1, direction=0):
    self.game_state = config.game_state

    self.speed      = speed
    self.direction  = direction

    if boundary:
      self.boundary   = pygame.Rect(boundary)
    else: 
      self.boundary = pygame.Rect((0,0), (config.screen_width, config.screen_height))
    #confine boundary to game area
    self.boundary = pygame.Rect.clip(self.boundary, self.game_state.rect)

    if not size:
      size = (100,100)

    if not position:
      position = self.boundary.center

    self.rect = pygame.Rect(position, size)

    self.inactive = False
    self.invisible = False
    self.delete = False

    self.inventory = {}
    self.armor = 1
    self.health = 100
    self.impact_power = 100
    self.type = self.Type.NEUTRAL
    
  # Move object according to speed and direction, within boundary
  def move(self, x=0, y=0, reflect=0):
    new_rect = self.rect.move(int(x),int(y))
    new_rect.clamp_ip(self.boundary)
    new_speed = [new_rect.x - self.rect.x, new_rect.y - self.rect.y]
    if reflect >= 0:
      new_x = int(x if new_speed[0] == x else -reflect * x)
      new_y = int(y if new_speed[1] == y else -reflect * y)

    self.rect = new_rect
    self.previous_speed = (x,y)
    return [new_x, new_y]

  def touch_boundary(self):
    return not self.boundary.contains(self.rect)

  # Move outside of object
  def uncollide_rect(self, obj_rect, gravity=0):
    x,y = 0, 0
    # Moving down
    if self.previous_speed[1] - gravity > 0:
      y = obj_rect.top - self.rect.bottom 
    # Moving up  
    elif self.previous_speed[1] < 0:  
      y = obj_rect.bottom - self.rect.top
    
    if y == 0 or self.gravity == 0: 
      # Moving right
      if self.previous_speed[0] > 0:
        x = obj_rect.left - self.rect.right
      # Moving left  
      elif self.previous_speed[0] < 0:  
        x = obj_rect.right - obj_rect.left 

  

    print("UCM",x,y)
    self.move(x,y)


  def vector2xy(self, direction, speed):
    radie = -math.radians(direction)
    x = speed * math.cos(radie)
    y = speed * math.sin(radie)
    return x,y

  # Mirror direction, when hittinh boundary
  def mirror_direction(self):
    if self.touch_boundary():
      # Left and Right side
      if self.rect.x == self.boundary.x or self.rect.x + self.rect.width == self.boundary.x + self.boundary.width:       
        self.direction = -self.direction + 180
      
      # bottom  and top
      if self.rect.y == self.boundary.y or self.rect.y + self.rect.height == self.boundary.y + self.boundary.height:       
        self.direction = -self.direction 
      
      # reduce angle to 0-360 degrees
      self.direction = ((self.direction + 360 ) % 360) // 1  
      # Change to oposite direction

  # Return true at random, on avarage at <freq> times pr. second
  def random_frequency(self, freq):
    return random.randint(0, config.frame_rate // freq ) == 0