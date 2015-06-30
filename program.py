import sys
from functions import fill_routes, rat_start_position, available_positions, throw_cat

maze_file = open('maze.txt' , 'r')
maze_costs_file = open('maze_costs.txt' , 'r')
maze = [ map(int,line.split(',')) for line in maze_file ]
maze_costs = [ map(int,line.split(',')) for line in maze_costs_file ]

routes = fill_routes(maze, maze_costs, 2, 3)
rat_start_position = rat_start_position(maze)
maze_available_positions = available_positions(maze)

print throw_cat(maze_available_positions)