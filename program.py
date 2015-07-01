import sys
from functions import *

maze_file = open('maze.txt' , 'r')
maze_costs_file = open('maze_costs.txt' , 'r')
maze = [ map(int,line.split(',')) for line in maze_file ]
maze_costs = [ map(int,line.split(',')) for line in maze_costs_file ]

exit_position = exit_position(maze)
routes = fill_routes(maze, maze_costs, exit_position[0], exit_position[1])
rat_position = rat_start_position(maze)
maze_available_positions = available_positions(maze)
changed_routes = None

while rat_position != exit_position:
    rat_position = go_rat(rat_position, routes)
    print "Brain is at " + `rat_position`
    if rat_position is None:
        break
    cat_position = generate_position(maze_available_positions)
    print "Cat is at " + `cat_position`
    changed_routes = throw_cat(maze, cat_position, routes, changed_routes)