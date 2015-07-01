import sys
import unittest
sys.path.append("..")
import functions

class TestGoRat(unittest.TestCase):
		def test_get_best_next_destination_when_there_is_a_way(self):
			position = (0, 0)
			routes = { (0, 0): { (0, 1): float('inf'), (1, 0): 6 } }

			self.assertEqual(functions.go_rat(position, routes), (1, 0))

		def test_get_none_destination_when_there_is_no_way(self):
			position = (0, 0)
			routes = { (0, 0): { (0, 1): float('inf'), (1, 0): float('inf') } }

			self.assertEqual(functions.go_rat(position, routes), None)
