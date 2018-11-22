
class Grid:

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height

    def in_bounds(self, position):
        (x, y) = position
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, position):
        (x, y) = position
        neighboring_nodes = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        valid_neighbors = filter(self.in_bounds, neighboring_nodes)
        return valid_neighbors
