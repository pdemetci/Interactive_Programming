from test_helper import unittest
from unittest import TestCase

from game_grid import GameGrid

class GameGridTest(TestCase):

    def testInit(self):
        g = GameGrid(4, 5)
        self.assertEqual(4, g.rows)
        self.assertEqual(5, g.cols)

    def testHandleGridClick(self):
        g = GameGrid(5, 5)
        row = 3
        col = 3

        cells = g.getChangedCells(row, col)
        prevVals = map(lambda rc: g.get(*rc), cells)

        g.handleGridClick(row, col)
        actualVals = map(lambda rc: g.get(*rc), cells)
        expectedVals = map(lambda x: x + 1, prevVals) 

        self.assertEqual(expectedVals, actualVals)

    def testGetChangedCells(self):
        g = GameGrid(5, 5)

        actualCells   = g.getChangedCells(0, 0)
        expectedCells = [(0, 0), (1, 0), (0, 1)]
        self.assertEqual(expectedCells, actualCells)

        actualCells   = g.getChangedCells(2, 0)
        expectedCells = [(2, 0), (1, 0), (3, 0), (2, 1)]
        self.assertEqual(expectedCells, actualCells)

        actualCells   = g.getChangedCells(2, 2)
        expectedCells = [(2, 2), (1, 2), (3, 2), (2, 1), (2, 3)]
        self.assertEqual(expectedCells, actualCells)

    def testIncrementCell(self):
        g = GameGrid(5, 5)
        row = 2
        col = 2

        prevVal = g.get(row, col)
        g.incrementCell(row, col)
        actualVal = g.get(row, col)
        expectedVal = 1
        self.assertEqual(expectedVal, actualVal)
       
        g.set(row, col, 6)
        prevVal = g.get(row, col)
        g.incrementCell(row, col)
        actualVal = g.get(row, col)
        expectedVal = 0
        self.assertEqual(expectedVal, actualVal)
       
if __name__ == "__main__":
    unittest.main()
