import pygame

class PygameGrid:
    def __init__(self, grid, resolution=(800, 800), line_width=3):
        pygame.init()
        self.grid = grid
        self.resolution = resolution
        self.line_width = line_width
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()

    def evaluate_dimensions(self):
        # Divide the resolution evenly among the cells, no explicit grid lines
        square_width = self.resolution[0] / self.cols if self.cols > 0 else 0
        square_height = self.resolution[1] / self.rows if self.rows > 0 else 0
        return (square_width, square_height)

    def convert_column_to_x(self, column, square_width):
        # No line width offset, just multiply
        return column * square_width

    def convert_row_to_y(self, row, square_height):
        # No line width offset, just multiply
        return row * square_height

    def draw_squares(self):
        from conways_game.cell_manager import CellState
        square_width, square_height = self.evaluate_dimensions()
        for row in range(self.rows):
            for column in range(self.cols):
                # Use cell state to determine color
                if self.grid[row][column] == CellState.ALIVE:
                    color = (255, 255, 255)  # White for alive
                else:
                    color = (0, 0, 0)  # Black for dead
                x = int(self.convert_column_to_x(column, square_width))
                y = int(self.convert_row_to_y(row, square_height))
                w = int(square_width)
                h = int(square_height)
                geometry = (x, y, w, h)
                pygame.draw.rect(self.screen, color, geometry)

    def run(self):
        running = True
        while running:
            self.clock.tick(15)
            self.screen.fill((0, 0, 0))
            self.draw_squares()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

    def pause(self):
        self.isPaused = True
        
        while self.isPaused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isPaused = False
        pygame.quit()
