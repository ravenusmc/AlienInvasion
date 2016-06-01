import sys
import pygame 

from menu import Menu
from pic import Tank

def run_game():
  pygame.init()
  settings = Menu()
  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
  pygame.display.set_caption("Review Version")

  color = (settings.bg_color)

  tank = Tank(screen)

  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()


    screen.fill(color)
    tank.blitme()

    pygame.display.flip()

run_game()

