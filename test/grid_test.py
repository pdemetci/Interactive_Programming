import test_helper
import unittest
from unittest import TestCase

from grid import Grid

class GridTest(TestCase):

    def testInit(self):
        g = Grid(4, 5)
        self.assertEqual(4, g.rows)
        self.assertEqual(5, g.cols)

    def testGet(self):
        g = Grid(5, 5)
        g.set(3, 3, 10)
        self.assertEqual(10, g.get(3, 3))

    def testSet(self):
        g = Grid(5, 5)
        g.set(3, 3, 10)
        self.assertEqual(10, g.get(3, 3))

if __name__ == "__main__":
    unittest.main()
