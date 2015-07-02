import sys
from random import randint

def available_positions(maze):
    positions = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] != 0:
                positions.append((row, col))

    return positions

def possible_back_moves(maze, current_row, current_col):
    possible = []
    next_row = current_row - 1
    next_col = current_col - 1
    if (next_row >= 0 and maze[next_row][current_col] != 0):
        possible.append((next_row, current_col))

    if (next_col >= 0 and maze[current_row][next_col] != 0):
        possible.append((current_row, next_col))

    return possible

def add_route(origin, destination, cost, routes):
    if origin in routes:
        routes[origin][destination] = cost
    else:
        routes[origin] = { destination: cost }

def fill_routes(maze, maze_costs, current_row, current_col, last_cost = 0, last_position = (), routes = {}):
    cost = maze_costs[current_row][current_col] + last_cost

    add_route((current_row, current_col), last_position, cost, routes)

    current_position = (current_row, current_col)
    for position in possible_back_moves(maze, current_row, current_col):
        fill_routes(maze, maze_costs, position[0], position[1], cost, current_position, routes)

    return routes

def generate_position(available_positions):
    drawn_position = available_positions[randint(0, len(available_positions)-1)]
    return drawn_position

def throw_cat(maze_costs, position):
    maze_costs[position[0]][position[1]] = float('inf')

def go_rat(position, routes):
    minimum = float('inf')
    next_route = None
    
    for route in routes[(position[0], position[1])]:
        route_cost = routes[(position[0], position[1])][route]
        if route_cost < minimum:
            minimum = route_cost
            next_route = route

    return next_route

def rat_start_position(maze):
    i = 0
    for row in maze:
        j = 0
        for elem in row:
            if elem == 'S':
                return (i, j)
            j += 1
        i += 1

def exit_position(maze):
    i = 0
    for row in maze:
        j = 0
        for elem in row:
            if elem == 'F':
                return (i, j)
            j += 1
        i += 1

def escape(maze, maze_costs, rat_position, exit_position, available_positions, routes, output = sys.stdout):
    while rat_position != exit_position:
        cat_position = generate_position(available_positions)
        output.write("Cat is at " + `cat_position` + "\n")

        if cat_position == rat_position:
            output.write("The cat caught the rat\n")
            break
        throw_cat(maze_costs, cat_position)
        routes = fill_routes(maze, maze_costs, exit_position[0], exit_position[1])

        rat_position = go_rat(rat_position, routes)
        if rat_position is None:
            output.write("There's no way to Brain\n")
            break
        else:
            output.write("Brain is at " + `rat_position` + "\n")