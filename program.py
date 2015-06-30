import sys
from functions import *

maze_file = open('maze.txt' , 'r')
maze_costs_file = open('maze_costs.txt' , 'r')
maze = [ map(int,line.split(',')) for line in maze_file ]
maze_costs = [ map(int,line.split(',')) for line in maze_costs_file ]

routes = fill_routes(maze, maze_costs, 2, 3)
rat_start_position = rat_start_position(maze)
maze_available_positions = available_positions(maze)

changed_routes = throw_cat(maze, (1, 0), routes)
throw_cat(maze, (1, 1), routes, changed_routes)
print routes