from conways_game.grid_manager import GridManager
from conways_game.grid_manager import CellManager
from conways_game.grid_manager import CellState

class GameOfLife:
    
    def __init__(self, rows, cols):
        self.grid_manager = GridManager(rows, cols)
