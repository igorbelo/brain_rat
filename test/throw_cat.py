import sys
import unittest
sys.path.append("..")
import functions

class TestThrowCat(unittest.TestCase):
		def test_if_throw_cat_changes_cost_to_inf(self):
			maze_costs = [[1, 2, 3, 4], [5, 6, 7, 8]]
			expected_maze_costs = [[1, 2, 3, 4], [5, float('inf'), 7, 8]]
			functions.throw_cat(maze_costs, (1, 1))
			self.assertEqual(maze_costs, expected_maze_costs)