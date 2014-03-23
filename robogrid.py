class Robot(object):
    def __init__(self, name):
        self._heading = 0

    def forward(self):
        pass

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
