class GameStats():
  #Track statistics for alien invasion

  def __init__(self, ai_settings):
    #init stats 
    self.ai_settings = ai_settings
    self.reset_stats()
    #Start alien invasion in an active state.
    self.game_active = True 

    #start game in an inactive state
    self.game_active = False

    #High score should never be reset
    self.high_score = 0

  def reset_stats(self):
    #init stats that can change during the game. 
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0
    