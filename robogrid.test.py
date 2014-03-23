import unittest

from robogrid import Robot

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
        start = r.y
        r.forward()
        self.assertEqual(start - 1, r.y)

        start = r.x
        r.left()
        r.forward()
        self.assertEqual(start - 1, r.x)


if __name__ == "__main__":
    unittest.main()
