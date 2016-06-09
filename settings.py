class Settings():
  #A class to store all the settings for alien invasion

  def __init__(self):
    #init the games settings.
    #screen settings
    self.screen_width = 1000
    self.screen_height = 700
    self.bg_color = (230, 230, 230)
    #ship settings 
    self.ship_speed_factor = 8
    self.ship_limit = 3
    #bullet settings
    self.bullet_speed_factor = 10
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60,60,60
    self.bullets_allowed = 3
    #alien settings
    self.alien_speed_factor = 100
    self.fleet_drop_speed = 10
    #fleet direction of 1 represents right, -1 represents left
    self.fleet_direction = 1

