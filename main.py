import random
from conways_game.conways_game_of_life import GameOfLife
from utils.json_reader import JsonReader

if __name__ == "__main__":
    rule_reader = JsonReader.read_json_file('rules_config.json')

    grid_height = rule_reader['height_rule']
    grid_width = rule_reader['width_rule']
    survival_min_rule = rule_reader['survival_min_rule']
    survival_max_rule = rule_reader['survival_max_rule']
    birth_rule = rule_reader['birth_rule']
    tick_rule = rule_reader['tick_rule']
    spawn_direction = rule_reader.get('initial_spawn_direction', 'bottom')
    spawn_rows = rule_reader.get('initial_spawn_rows', 4)
    alive_percentage = rule_reader.get('initial_alive_percentage', 0.4)
    continuous_spawn_rate = rule_reader.get('continuous_spawn_rate', 0.0)
    continuous_spawn_direction = rule_reader.get('continuous_spawn_direction', 'none')

    dimension_rule_arr = [grid_height, grid_width]
    survival_rule_arr = [survival_min_rule, survival_max_rule, birth_rule]
    game_rule_arr = [tick_rule]


    print(f'grid_height: {grid_height}, grid_width: {grid_width}')

    game = GameOfLife(dimension_rule_arr, survival_rule_arr)
    
    # Set continuous spawning configuration
    game.env_manager.continuous_spawn_rate = continuous_spawn_rate
    game.env_manager.continuous_spawn_direction = continuous_spawn_direction
    
    # Initialize with random cells based on configuration
    random_cells = []
    
    if spawn_direction == "bottom":
        for i in range(grid_height - spawn_rows, grid_height):
            for j in range(grid_width):
                if random.random() < alive_percentage:
                    random_cells.append((i, j))
    elif spawn_direction == "top":
        for i in range(spawn_rows):
            for j in range(grid_width):
                if random.random() < alive_percentage:
                    random_cells.append((i, j))
    elif spawn_direction == "left":
        for i in range(grid_height):
            for j in range(spawn_rows):
                if random.random() < alive_percentage:
                    random_cells.append((i, j))
    elif spawn_direction == "right":
        for i in range(grid_height):
            for j in range(grid_width - spawn_rows, grid_width):
                if random.random() < alive_percentage:
                    random_cells.append((i, j))
    
    game.env_manager.set_initial_pattern(random_cells)
    
    game.run(game_rule_arr);