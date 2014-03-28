class Grid(dict):
    def __init__(self, grid):
        self.width, self.height = len(grid), len(grid[0])
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                self[(row_index, col_index)] = cell

    def __iter__(self):
        for row in range(self.height):
            yield [self[row, col] for col in range(self.width)]

    def __repr__(self):
        return "<Grid of size {w}x{h}>".format(w=self.width,
                                               h=self.height)

    def __str__(self):
        return "\n".join("".join(self.char(col) for col in row) for row in self)

    def char(self, state):
        return "#" if state else "."

    def free_position(self):
        for x in range(self.width):
            for y in range(self.height):
                if self[x, y] == False:
                    return x, y
        return None

class Simple_Grid(Grid):
    def __init__(self, size):
        super(type(self), self).__init__(make_grid(size, False))

class Maze(Grid):
    def __init__(self, size):
        if size < 5:
            raise ValueError("Grid size must be >= 5 to make a maze")
        super(type(self), self).__init__(make_grid(size, pattern_s_maze))

def make_grid(size, contents=None):
    if callable(contents):
        value_func = contents
    else:
        contents = True if contents == None else contents
        value_func = lambda x, y, size: contents

    f = cell_value(size, value_func)
    return [[f(x, y) for x in range(size)] for y in range(size)]

def cell_value(size, value_func):
    def cell_value_inner(x, y):
        if border(x, y, size):
            return True
        return value_func(x, y, size)
    return cell_value_inner

def border(x, y, size):
    return x == 0 or y == 0 or x == size - 1 or y == size - 1

def pattern_s_maze(x, y, size):
    if x % 2 == 1:
        return False

    if y == 1:
        return x in range(2, size + 1, 4)
    elif y == size - 2:
        return x in range(0, size + 1, 4)


    return True
