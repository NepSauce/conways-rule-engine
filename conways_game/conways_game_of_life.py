import pygame
import time
from conways_game.env_manager import EnvManager
from conways_game.pygame_module.pygame_grid import PygameGrid

class GameOfLife:
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.env_manager = EnvManager(dimension_rule_arr, survival_rule_arr)
        self.pygame_grid = PygameGrid(self.env_manager.grid)
        self.dimension_rule_arr = dimension_rule_arr
        self.survival_rule_arr = survival_rule_arr
        self.isPaused = False

    def run(self, game_rule_arr):
        tick_rate = game_rule_arr[0]
        running = True
        
        while running:
            time.sleep(1 / tick_rate)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if not self.isPaused:
                self.update()
                self.render()
        
        pygame.quit()

    def update(self):
        self.env_manager.update_grid()
        self.pygame_grid.grid = self.env_manager.grid
        self.pygame_grid.rows = len(self.env_manager.grid)
        self.pygame_grid.cols = len(self.env_manager.grid[0]) if self.pygame_grid.rows > 0 else 0

    def render(self):
        self.pygame_grid.screen.fill((0, 0, 0))
        self.pygame_grid.draw_squares()
        pygame.display.flip()


    def pause(self):
        self.isPaused = True
        self.pygame_grid.pause()