from conways_game.env_manager import EnvManager
from conways_game.cell_manager import CellManager
from conways_game.pygame_module.pygame_grid import PygameGrid

class GameOfLife:
    
    def __init__(self, rows, cols):
        self.env_manager = EnvManager(rows, cols)
        self.pygame_grid = PygameGrid(self.env_manager.grid)
        self.height_rule = rows
        self.width_rule = cols
        self.isPaused = False

    def run(self):
        self.pygame_grid.run()

        while not self.isPaused:
            self.update(self.height_rule, self.width_rule)
            self.render()

    def update(self, height_rule, width_rule):
        self.env_manager.update_grid(height_rule, width_rule)

    def render(self):
        self.pygame_grid.draw_squares()


    def pause(self):
        self.isPaused = True
        self.pygame_grid.pause()