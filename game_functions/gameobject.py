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
    # Make sure the new rectangle is contained within the boundary
    new_rect.clamp_ip(self.boundary)
    # Update the speed to the actual movement. 
    new_speed = [new_rect.x - self.rect.x, new_rect.y - self.rect.y]
    if reflect >= 0:
      new_x = int(x if new_speed[0] == x else -reflect * x)
      new_y = int(y if new_speed[1] == y else -reflect * y)

    self.rect = new_rect
    self.previous_speed = (x,y)
    return [new_x, new_y]

  # Test if rect touches the boundary
  def touch_boundary(self):
    return not self.boundary.contains(self.rect)

  # Move outside of object. Called on collission.
  # self.previous_speed should hold the speed that caused a collission from a free position
  def uncollide_rect(self, obj_rect, gravity=0,reflect=0):
    reverse = [0,0]
    vertical_move = self.speed[1] >= self.speed[0]

    if vertical_move:
      # Moving down from above object, move back up on top
      if self.previous_speed[1] > 0 :
        if self.rect.bottom >= obj_rect.top:
          # print("landed on top")
          reverse[1] = obj_rect.top - self.rect.bottom
      
        # Moving up from below object, move to beloe bottom
      else:   
        if self.rect.top >= obj_rect.bottom:
          # Move on top
          reverse[1] = obj_rect.bottom - self.rect.top
          print("Bumped from below",reverse)

      # Move horizontally back at the same ratio
      #if reverse[1] != 0 and self.previous_speed[0] != 0:
      #  reverse[0] = self.previous_speed[0] * reverse[1] / self.previous_speed[1]

      # Check if self rect is over the side horizontally
      if self.rect.right + reverse[0] < obj_rect.left or self.rect.left + reverse[0] > obj_rect.right:
        vertival_move = False
        reverse = [0,0]
        print("skift til horisontal")

    if not vertical_move:
      # hitting from the left side
      if self.previous_speed[0] > 0:
        reverse[0] = obj_rect.left - self.rect.right 
        print("hitting from the left",reverse)

      # hitting from the right side  
      else:
        reverse[0] = obj_rect.right - self.rect.left
        print("Hitting from the right",reverse)

      # Move vertically back at the same ratio
      #if reverse[0] != 0 and self.previous_speed[1] != 0:
        #reverse[1] = self.previous_speed[1] * reverse[0] / self.previous_speed[0]
        #pass

    #print("UCM",reverse[0],reverse[1],self.previous_speed, gravity)
    self.move(reverse[0],reverse[1])
    return reverse


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