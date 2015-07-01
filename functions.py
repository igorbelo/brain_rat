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
        if destination in routes[origin]:
            if cost < routes[origin][destination]:
                routes[origin][destination] = cost
        else:
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

def throw_cat(maze, position, routes):
    back_moves = possible_back_moves(maze, position[0], position[1])
    for back_move in back_moves:
        routes[back_move][(position[0], position[1])] = float('inf')
        throw_cat(maze, back_move, routes)

    return routes

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