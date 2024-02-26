import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(3,5), 8)