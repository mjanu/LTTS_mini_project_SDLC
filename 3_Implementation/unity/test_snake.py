import unittest
from snake import game1

class TestSnake(unittest.TestCase):
    def test_snake(self):
        self.assertAlmostEqual(game1(4,4),3)