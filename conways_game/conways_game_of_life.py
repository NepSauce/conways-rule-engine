from conways_game.env_manager import EnvManager

class GameOfLife:
    
    def __init__(self, rows, cols):
        self.env_manager = EnvManager(rows, cols)
