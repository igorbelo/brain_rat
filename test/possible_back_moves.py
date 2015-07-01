import sys
import unittest
sys.path.append("..")
import functions

class TestBackMoves(unittest.TestCase):
		def setUp(self):
			self.maze = [[0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]

		def test_without_back_moves(self):
			expected_possible_back_moves = []
			self.assertEqual(functions.possible_back_moves(self.maze, 1, 2), expected_possible_back_moves)

		def test_with_back_moves_from_2_3_position(self):
			expected_possible_back_moves = [(2, 2), (1, 3)]
			self.assertItemsEqual(functions.possible_back_moves(self.maze, 2, 3), expected_possible_back_moves)		