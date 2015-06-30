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

def throw_cat(maze, position, routes, changed_routes = None):
    if changed_routes is not None:
        for route in changed_routes:
            routes[route.keys()[0]] = route.values()[0]

    changed_routes = []
    for back_position in possible_back_moves(maze, position[0], position[1]):
        changed_routes.append({ (back_position[0], back_position[1]): { (position[0], position[1]): routes[(back_position[0], back_position[1])][(position[0], position[1])] } })
        routes[(back_position[0], back_position[1])][(position[0], position[1])] = float('inf')

    return changed_routes


def rat_start_position(maze):
    return (0, 0)