"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame
from game_functions import animation
import config

# Settings
background_color = (16,64,96)
color = (0,82,255)
font_name = 'freesansbold.ttf'
  
# Dashboard
# Depending on child class using helth, score and level variables
class Dashboard:
  def __init__(self, game_state):
    # Store referance to game state
    self.game_state = game_state

    # Set dashboard dimensions
    height = config.screen_height // 15
    self.rect = pygame.Rect(0, config.screen_height - height, config.screen_width, height)

    # Create a font 
    self.font = pygame.font.Font( font_name, height // 2 )
 
  def draw(self, surface):
    # Paint background
    surface.fill(background_color, self.rect)

   