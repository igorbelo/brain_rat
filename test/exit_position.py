import sys
import unittest
sys.path.append("..")
import functions

class TestExitPosition(unittest.TestCase):
		def test_exit_position_when_F_is_at_2_2(self):
			maze = [['S', 1, 0, 1], [0, 0, 1, 1], [1, 1, 'F', 1]]
			self.assertEqual(functions.exit_position(maze), (2, 2))

		def test_exit_position_when_F_is_at_2_3(self):
			maze = [[0, 'S', 0, 1], [0, 0, 1, 1], [1, 1, 1, 'F']]
			self.assertEqual(functions.exit_position(maze), (2, 3))