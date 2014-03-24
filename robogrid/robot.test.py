import unittest

from robot import Robot
from grids import Simple_Grid

class Test_Robot(unittest.TestCase):
    def test_basic_turning(self):
        r = Robot("Tesla")
        r.left()
        self.assertEqual(3, r.heading)
        r.left()
        self.assertEqual(2, r.heading)
        r.right()
        r.right()
        self.assertEqual(0, r.heading)

    def test_basic_movement(self):
        r = Robot("Tesla")

        for i in range(2):
            r.right()
            r.forward()

        r.right()
        r.right()

        x, y = r.pos
        r.forward()
        self.assertEqual((x, y - 1), r.pos)

        x, y = r.pos
        r.left()
        r.forward()
        self.assertEqual((x - 1, y), r.pos)

    def test_simple_grid(self):
        r = Robot("Tesla", Simple_Grid(3))
        pos = r.x, r.y
        r.forward()
        self.assertEqual(pos, r.pos)
        r.backward()
        r.left()
        r.forward()
        self.assertEqual(pos, r.pos)

    def test_move_forward_check(self):
        r = Robot("Tesla", Simple_Grid(3))
        self.assertEqual(False, r.can_move_forward())

        r = Robot("Tesla", Simple_Grid(5))
        r.right()
        self.assertEqual(True, r.can_move_forward())
if __name__ == "__main__":
    unittest.main()
