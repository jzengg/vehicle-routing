from car import Car

class Grid:

    def __init__(self, x=10, y=10):
        self.grid = [[None for i in range(x)] for j in range(y)]
        # assume that car starts near center of grid, or randomly select a point?
        midpoint = (x // 2, y // 2)
        self.grid[midpoint[0]][midpoint[1]] = Car()

    def print_state(self):
        output = ''
        for row in self.grid:
            output += (' ').join(str(point) if point else '|' for point in row)
            output += '\n'
        print(output)




g = Grid()
c = Car()
g.print_state()
