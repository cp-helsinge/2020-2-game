"""============================================================================

pygame has some issues with linux, selecting the right sound card

List sound cards:
  cat /proc/asound/cards 


edit the .asoundrc file to reflect the sound card you wan to use. (PCM)

Also make sure these libs are installed:

apt-get install python-pygame
sudo apt-get install libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sudo sdl-config --cflags --libs

https://stackoverflow.com/questions/32533585/pygame-projects-wont-run-pygame-error-no-available-video-device

============================================================================"""
import pygame
import os 
import config

# Class for in-game sound effects
class Sound:
  mixer_init = False

  def __init__(self, file_name):
    if not Sound.mixer_init:
      self.init()

    try:
      self = pygame.mixer.Sound(os.path.join(config.sound_path, name) )

    except Exception as ex:
      print("Failed to use pygame mixer",ex)
      # Make a dummy play method, to avoid error messages when sound fails (Mostly on unix)
      def play():
        pass
      self.play = play

  def init():
    if not Sound.mixer_init:
      try:
        pygame.mixer.init(allowedchanges=0)
        Sound.mixer_init = True
        pygame.mixer.music.set_volume(config.sound_volume)
      except Exception as ex:
        print("Failed to use pygame mixer",ex)
  

# Class for backgound music    
class Music:
  is_paused = False

  def __init__(self, file_name = None):
    if not Sound.mixer_init:
      Sound.init()


    self.load(file_name)
    self.play()

  def load(self, file_name):
    print("Loading music",file_name)
    if file_name:
      try:
        pygame.mixer.music.load(os.path.join(config.sound_path, file_name))
      except Exception as ex:
        print("failed to load music",ex, "using sound file:", file_name)


  def play(loops=-1, start=0.0, fade_ms = 500):
    try:
      #pygame.mixer.music.play(loops, start, fade_ms)
      #pygame.mixer.music.play(loops=loops, start=start, fade_ms =fade_ms)
      pygame.mixer.music.play()
      Music.is_paused = False
    except Exception as ex:
      print("failed to play music:",ex)

  def pause(self):
    try:
      # Se if music is loaded
      if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        Music.is_paused = True
    except Exception as ex:
      print("failed to pause music:",ex)

  def unpause(self):
    try:
      # Se if music is loaded
      if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        Music.is_paused = False
    except Exception as ex:
      print("failed to unpause music:",ex)


  def toggle(self):
    if Music.is_paused:
      self.play()
    else:
      self.pause()  

  def stop(self):
    try:
      pygame.mixer.music.fadeout(500)
      Music.is_paused = False
    except Exception as ex:
      print("failed to stop music:",ex)


    