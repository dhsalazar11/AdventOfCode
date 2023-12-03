import regex as re
from functools import reduce

bagMax = {"red": 12, "green": 13, "blue": 14}

def part_one(input: str) -> int:
    input_array = re.sub('[,:;]', '', input).split()
    games_block_count = {}
    game_id = -1
    
    for i, current in enumerate(input_array):
        if current == "Game":
            game_id = int(input_array[i + 1])
            games_block_count[game_id] = {"red": 0, "green": 0, "blue": 0}
        elif current in bagMax:
            games_block_count[game_id][current] = max(games_block_count[game_id][current], int(input_array[i - 1]))
 
    idSum = sum(key for key, val in games_block_count.items() if all(bagMax[k] - v >= 0 for k, v in val.items()))
    return idSum

def part_two(input: str) -> int:
    input_array = re.sub('[,:;]', '', input).split()
    games_block_count = {}
    game_id = -1
    
    for i, current in enumerate(input_array):
        if current == "Game":
            game_id = int(input_array[i + 1])
            games_block_count[game_id] = {"red": 0, "green": 0, "blue": 0}
        elif current in bagMax:
            games_block_count[game_id][current] = max(games_block_count[game_id][current], int(input_array[i - 1]))
    
    set_power_sum = sum(reduce(lambda x, y: x * y, val.values(), 1) for val in games_block_count.values())
    return set_power_sum
                        
if __name__ == "__main__":
    file = open("data/day2.txt", "r")
    puzzle_input = file.read()
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))