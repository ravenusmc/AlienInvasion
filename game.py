import pygame
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard 
from button import Button
from ship import Ship
from alien import Alien 
from pygame.sprite import Group 

def run_game():
  #inits game and creates a screen object.
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  #Make the Play Button
  play_button = Button(ai_settings, screen, "Play")

  #Create an instance to store game stats and create a scoreboard 
  stats = GameStats(ai_settings)
  sb = Scoreboard(ai_settings, screen, stats)

  #make a ship
  ship = Ship(ai_settings, screen)
  #Make a group to store bullets in. 
  bullets = Group()
  #make an alien.
  aliens = Group()

  #Creating a fleet of aliens
  gf.create_fleet(ai_settings, screen, ship, aliens)


  #Start the main loop for the game.
  while True:
    gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
    
    if stats.game_active:
      ship.update()
      gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
      gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

