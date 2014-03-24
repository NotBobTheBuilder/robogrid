from grids import Infinite_Grid

class Robot(object):
    def __init__(self, name, grid=None):
        if grid == None:
            grid = Infinite_Grid()
        self.grid = grid

        start_pos = self.grid.free_position()
        if start_pos == None:
            raise ValueError("No space in proposed grid")

        self._heading = 0
        self._x, self._y = start_pos

    def forward(self):
        if self.heading == 0:
            self._y -= 1
        elif self.heading == 1:
            self._x += 1
        elif self.heading == 2:
            self._y += 1
        elif self.heading == 3:
            self._x -= 1

    def right(self):
        self.heading += 1

    def left(self):
        self.heading -= 1

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, val):
        self._heading = val % 4

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def pos(self):
        return self.x, self.y
