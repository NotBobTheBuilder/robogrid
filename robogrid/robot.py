from .grids import Simple_Grid

class Robot(object):
    def __init__(self, name, grid=None):
        self.name = name

        if grid == None:
            grid = Simple_Grid(20)
        self.grid = grid

        start_pos = self.grid.free_position()
        if start_pos == None:
            raise ValueError("No space in proposed grid")

        self._heading = 0
        self._x, self._y = start_pos

    def __repr__(self):
        summary = {
            "name": self.name,
            "grid": repr(self.grid)
        }
        return 'Robot("{name}", {grid})'.format(**summary)

    def __str__(self):
        arrow = "^>!<"[self.heading]
        result = ""
        for row_i, row in enumerate(self.grid):
            for col_i, cell in enumerate(row):
                if (row_i, col_i) == self.pos:
                    result += arrow
                else:
                    result += self.grid.char(cell)
            result += "\n"
        return result

    def forward(self):
        if self.heading == 0:
            if self.grid[self.x, self.y-1] == False:
                self._y -= 1
        elif self.heading == 1:
            if self.grid[self.x+1, self.y] == False:
                self._x += 1
        elif self.heading == 2:
            if self.grid[self.x, self.y+1] == False:
                self._y += 1
        elif self.heading == 3:
            if self.grid[self.x-1, self.y] == False:
                self._x -= 1

    def can_move_forward(self):
        if self.heading == 0:
            return self.grid[self.x, self.y-1] == False
        elif self.heading == 1:
            return self.grid[self.x+1, self.y] == False
        elif self.heading == 2:
            return self.grid[self.x, self.y+1] == False
        elif self.heading == 3:
            return self.grid[self.x-1, self.y] == False

    def backward(self):
        self.right()
        self.right()
        self.forward()
        self.right()
        self.right()

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
