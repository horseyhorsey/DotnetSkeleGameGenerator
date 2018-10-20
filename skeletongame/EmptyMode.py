import procgame.game
from procgame.game import AdvancedMode
import logging


class EmptyMode(procgame.game.AdvancedMode):
    """
    EmptyMode
    """
    def __init__(self, game):

        super(EmptyMode, self).__init__(game=game, priority=2, mode_type=AdvancedMode.Game)
        self.logger = logging.getLogger('EmptyMode')
    
    def mode_started(self):
        self.logger.debug("EmptyMode started")
    
    def mode_stopped(self): 
        self.logger.debug("EmptyMode ended")


 
  