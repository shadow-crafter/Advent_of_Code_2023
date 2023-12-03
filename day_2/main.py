import math

id_sum = 0
cube_power_total = 0
set_powers = []

def process_input(line):
        game_split = line.strip().split(": ")
        game_id = int(game_split[0].split()[1])
        
        bag_split = game_split[1].split("; ")
        cube_list = []
        for set in bag_split:
            cube_list.append(set.split(", "))
        
        return game_id, cube_list

def get_answers(cube_list):
    highest_colors = {"red": 0, "green": 0, "blue": 0}
    game_possible = True

    for color_set in cube_list:
        for color_lst in color_set:
            color_split = color_lst.split()
            color = color_split[1]
            color_value = int(color_split[0])
            
            if color == "red" and color_value > 12:
                game_possible = False
            elif color == "green" and color_value > 13:
                game_possible = False
            elif color == "blue" and color_value > 14:
                game_possible = False
            
            if color_value > highest_colors[color]:
                highest_colors[color] = color_value
    
    cube_powers = math.prod(list(highest_colors.values()))
    return game_possible, cube_powers

with open("input.txt") as f:
    for line in f:
        game_id, cube_list = process_input(line)
        game_possible, cube_powers = get_answers(cube_list)
        
        if game_possible:
            id_sum += game_id
        cube_power_total += cube_powers

        print(f"Game {game_id}: list: {cube_list}. Game is possible: {game_possible}, cubes powers: {cube_powers}")

print(f"Id sum is: {id_sum}, total cube powers is {cube_power_total}")
