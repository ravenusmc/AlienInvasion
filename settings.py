class Settings():
  #A class to store all the settings for alien invasion

  def __init__(self):
    #init the games settings.

    #screen settings
    self.screen_width = 1000
    self.screen_height = 700
    self.bg_color = (230, 230, 230)

    #ship settings 
    self.ship_limit = 3

    #bullet settings
    self.bullet_speed_factor = 10
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60,60,60
    self.bullets_allowed = 3

    #alien settings
    self.fleet_drop_speed = 10

    #How quickly the game speeds up
    self.speedup_scale = 1.1

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    #Init settings that change throughout the game 
    self.ship_speed_factor = 8
    self.bullet_speed_factor = 15 
    self.alien_speed_factor = 5 

    #fleet direction of 1 represents right, -1 represents left
    self.fleet_direction = 1

  def increase_speed(self):
    #Increase speed settings 
    self.ship_speed_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale



