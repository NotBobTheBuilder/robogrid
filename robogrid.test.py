import unittest

from robogrid import Robot

class Test_Robot(unittest.TestCase):
    def test_basic_turning(self):
        r = Robot("Tesla")
        r.heading = 0
        r.left()
        self.assertEqual(270, r.heading)
        r.left()
        self.assertEqual(180, r.heading)
        r.right()
        r.right()
        self.assertEqual(0, r.heading)

if __name__ == "__main__":
    unittest.main()
