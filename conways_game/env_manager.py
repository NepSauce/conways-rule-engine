import random
from conways_game import cell_manager
from conways_game.cell_manager import CellState 
from conways_game.cell_manager import CellManager


class EnvManager: 
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.cell_manager = CellManager(dimension_rule_arr, survival_rule_arr)
        self.dimension_rule_arr = dimension_rule_arr
        self.survival_rule_arr = survival_rule_arr
        self.grid = [[CellState.DEAD for _ in range(dimension_rule_arr[1])] 
                     for _ in range(dimension_rule_arr[0])]
        self.continuous_spawn_rate = 0.0
        self.continuous_spawn_direction = 'none'
    
    def set_initial_pattern(self, pattern_coords):
        for row, col in pattern_coords:
            if 0 <= row < self.dimension_rule_arr[0] and 0 <= col < self.dimension_rule_arr[1]:
                self.grid[row][col] = CellState.ALIVE

    def update_grid(self):
        # Set the current grid in cell_manager
        self.cell_manager.grid = self.grid
        next_grid = [[CellState.DEAD for _ in range(self.dimension_rule_arr[1])] 
                    for _ in range(self.dimension_rule_arr[0])]
        
        for i in range(self.dimension_rule_arr[0]):
            for j in range(self.dimension_rule_arr[1]):
                next_grid[i][j] = self.cell_manager.determine_next_state(
                    (i, j), self.survival_rule_arr[0], 
                    self.survival_rule_arr[1], [self.survival_rule_arr[2]])
        
        if self.continuous_spawn_rate > 0:
            if self.continuous_spawn_direction == "bottom":
                for j in range(self.dimension_rule_arr[1]):
                    if random.random() < self.continuous_spawn_rate:
                        next_grid[self.dimension_rule_arr[0] - 1][j] = CellState.ALIVE
            elif self.continuous_spawn_direction == "top":
                for j in range(self.dimension_rule_arr[1]):
                    if random.random() < self.continuous_spawn_rate:
                        next_grid[0][j] = CellState.ALIVE
            elif self.continuous_spawn_direction == "left":
                for i in range(self.dimension_rule_arr[0]):
                    if random.random() < self.continuous_spawn_rate:
                        next_grid[i][0] = CellState.ALIVE
            elif self.continuous_spawn_direction == "right":
                for i in range(self.dimension_rule_arr[0]):
                    if random.random() < self.continuous_spawn_rate:
                        next_grid[i][self.dimension_rule_arr[1] - 1] = CellState.ALIVE
                
        self.grid = next_grid
        return self.grid

