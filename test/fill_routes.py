import sys
import unittest
sys.path.append("..")
import functions

class TestAddRoute(unittest.TestCase):
			def test_routes_fill_1(self):
					maze = [['S', 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 'F', 0, 0]]
					maze_costs = [[1, 2, 5, 0, 0], [0, 2, 1, 0, 0], [0, 1, 4, 0, 0]]
					expected_routes = {(1, 2): {(2, 2): 5}, (0, 1): {(0, 2): 12, (1, 1): 9}, (0, 0): {(0, 1): 10}, (2, 1): {(2, 2): 5}, (1, 1): {(1, 2): 7, (2, 1): 7}, (2, 2): {(): 4}, (0, 2): {(1, 2): 10}}

					self.assertEqual(functions.fill_routes(maze, maze_costs, 2, 2), expected_routes)

			def test_routes_fill_2(self):
					maze = [['S', 1, 1], [0, 1, 1], [0, 1, 'F']]
					maze_costs = [[1, 2, 5], [0, 2, 1], [0, 1, 4]]
					expected_routes = {(0, 0): { (0, 1): 10}, (0, 1): { (0, 2): 12, (1, 1): 9 }, (0, 2): { (1, 2): 10 }, (1, 1): { (1, 2): 7, (2, 1): 7 }, (1, 2): { (2, 2): 5 }, (2, 1): { (2, 2): 5 }, (2, 2): { (): 4 } }

					self.assertEqual(functions.fill_routes(maze, maze_costs, 2, 2), expected_routes)