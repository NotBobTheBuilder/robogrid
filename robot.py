class Robot(object):
    def __init__(self, name):
        self._heading = 0
        self.x = 0
        self.y = 0

    def forward(self):
        if self.heading == 0:
            self.y -= 1
        elif self.heading == 1:
            self.x += 1
        elif self.heading == 2:
            self.y += 1
        elif self.heading == 3:
            self.x -= 1

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
