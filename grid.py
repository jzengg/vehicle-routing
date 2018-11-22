
class Grid:

    def __init__(self, width=10, height=10, car_position=None):
        self.width = width
        self.height = height
        # assume that car starts near center of state, or randomly select a point?
        if car_position is None:
            car_position = (width // 2, height // 2)
        self.car_position = car_position

    def car_position(self):
        return self.car_position

    def move_car(self, position):
        self.car_position = position

    def in_bounds(self, position):
        (x, y) = position
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, position):
        (x, y) = position
        neighboring_nodes = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        valid_neighbors = filter(self.in_bounds, neighboring_nodes)
        return valid_neighbors
