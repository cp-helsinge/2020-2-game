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
    # Store current position
    pos = self.rect.topleft
    
    self.rect = self.rect.move(int(x),int(y))

    # Make sure the new rectangle is contained within the boundary
    self.rect.clamp_ip(self.boundary)

    # Update the speed to the actual movement. 
    self.previous_speed =  [self.rect.x - pos[0], self.rect.y - pos[1]]

    return self.previous_speed

  # Test if rect touches the boundary
  def touch_boundary(self):
    return not self.boundary.contains(self.rect)

  def uncollide_rect(self, obj_rect, gravity):
  # Move outside of object. Called on collission.
  # self.previous_speed should hold the speed that caused a collission from a free position
     # Find ascend ration of movement
    dx = abs(self.previous_speed[0])
    dy = abs(self.previous_speed[1])
    # Test for zero values
    asc = dx / dy if dx != 0 and dy != 0 else 0 if dx == 0 else 1000

    # Find:
    # * x value to move, to avoid collission
    # * x value of nearest side of object
    if self.previous_speed[0] < 0:
      x1 = obj_rect.right
      x2 = self.rect.left
    else:
      x1 = obj_rect.left
      x2 = self.rect.right
    x = int(x1 - x2)

    # Find:
    # * y value to move, to avoid collission
    # * y value of nearest side of object
    if self.previous_speed[1] > 0: 
      y1 = obj_rect.top
      y2 = self.rect.bottom
    else:  
      y1 = obj_rect.bottom
      y2 = self.rect.top
    y = int(y1 - y2)

    # Find out which side of object is hit first
    if y != 0 and abs(x / y) < abs(asc):
      y = int(self.previous_speed[1] * x / self.previous_speed[0])
      #print("horisontal impact",x,y)

    else:
      if y == -gravity:
        x = 0  
      elif y!= 0:  
        x = int(self.previous_speed[0] * asc)
      #print("vertical impact",x, y)

    self.rect.x = self.rect.x + x
    self.rect.y = self.rect.y + y
    self.previous_speed = [self.previous_speed[0] - x,self.previous_speed[1] -y]
    #print(x,y)
  

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