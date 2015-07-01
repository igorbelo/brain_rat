import sys
import unittest
sys.path.append("..")
import functions

class TestAvailablePositions(unittest.TestCase):
		def test_available_positions(self):
			maze = [[0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
			expected_available_positions = [(0, 1), (0, 3), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
			self.assertEqual(functions.available_positions(maze), expected_available_positions)