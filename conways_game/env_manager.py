class GridManager:
    
    def __init__(self, rows, cols):
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]
    
    def set_cell(self, row_index, col_index, state):
        self.grid[row_index][col_index] = state

class CellManager:
    
    def __init__(self):
        pass

    def count_live_neighbors(self, grid, row_index, col_index):
        live_neightbors = 0
        for i in range ()

class CellState:
    ALIVE = True
    DEAD = False