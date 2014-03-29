import unittest

from robogrid.grids import Grid, Simple_Grid
from robogrid import Robot

class Test_Grids(unittest.TestCase):
    def test_str(self):
        grid = Grid([[True, False], [False, True]])
        self.assertEqual("#.\n.#", str(grid))

    def test_simple_grid(self):
        grid = Simple_Grid(3)
        self.assertEqual("###\n#.#\n###", str(grid))

    def test_free_space(self):
        grid = Simple_Grid(5)
        self.assertEqual((1, 1), grid.free_position())
        grid = Simple_Grid(2)
        self.assertEqual(None, grid.free_position())
