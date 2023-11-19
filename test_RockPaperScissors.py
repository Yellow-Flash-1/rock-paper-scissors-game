import unittest
from random import randint
from RockPaperScissors import *

class TestRPS(unittest.TestCase):
	def test_rps_judge(self):
		self.assertEqual(rps_judge(0, 0), 0) # Test for a tie
		self.assertEqual(rps_judge(0, 1), 2) # Test for player 2 winning
		self.assertEqual(rps_judge(0, 2), 1) # Test for player 1 winning

	def test_user_choice(self):
		self.assertEqual(user_choice('R'), 0)
		self.assertEqual(user_choice('P'), 1)
		self.assertEqual(user_choice('S'), 2)
		self.assertRaises(ValueError, user_choice, 'X') # Test for invalid choice

if __name__ == '__main__':
	unittest.main()
