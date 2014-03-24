class Grid(dict):
    def __init__(self, grid):
        self.width, self.height = len(grid), len(grid[0])
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                self[(row_index, col_index)] = cell

    def __iter__(self):
        for row in range(self.height):
            yield [self[row, col] for col in range(self.width)]

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
        grid = self.bordered_grid(size)
        super(Simple_Grid, self).__init__(grid)

    def bordered_grid(self, size):
        grid = []
        border = [True] * size
        grid.append(border)
        for i in range(size - 2):
            grid.append([i == 0 or i == size-1 for i in range(size)])
        grid.append(border)
        return grid

class Infinite_Grid(Grid):
    def __init__(self):
        self.width  = 1
        self.height = 1

    def __getitem__(self, index):
        return False
