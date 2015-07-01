import sys
import unittest
sys.path.append("..")
import functions

class TestRatStartPosition(unittest.TestCase):
		def test_rat_start_position_when_S_is_at_0_0(self):
			maze = [['S', 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
			self.assertEqual(functions.rat_start_position(maze), (0, 0))

		def test_rat_start_position_when_S_is_at_0_1(self):
			maze = [[0, 'S', 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
			self.assertEqual(functions.rat_start_position(maze), (0, 1))