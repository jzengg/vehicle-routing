from grid import Grid
import collections

class Navigation:

    def __init__(self, grid, car_position):
        self.grid = grid
        # assume that car starts near center of state, or randomly select a point?
        if car_position is None:
            car_position = (grid.width // 2, grid.height // 2)
        self.car_position = car_position

        self.passenger = None
        self.location_passenger_map = {}
        self.queued_path = collections.deque()

    def advance_time(self, requests=None):
        if requests is None:
            requests = []
        for request in requests:
            location = request['start']
            self.location_passenger_map[location] = request

        # print('current position {}'.format(self.car_position))

        if not self.passenger:
            self.pickup_passenger()

        if self.queued_path:
            new_position = self.queued_path.pop()
            print('new position: {}'.format(new_position))
            self.move_car(new_position)

        if self.passenger:
            passenger_pickup, passenger_dropoff = self.passenger['start'], self.passenger['end']
            if self.car_position == passenger_pickup:
                print('picked up {}'.format(self.passenger['name']))
                self.queue_path(passenger_dropoff)
            elif self.car_position == passenger_dropoff:
                print('dropped off {}'.format(self.passenger['name']))
                self.passenger = None

    def move_car(self, position):
        self.car_position = position

    def pickup_passenger(self):
        self.passenger = self.nearest_passenger()
        if self.passenger:
            self.location_passenger_map.pop(self.passenger['start'])
            destination = self.passenger['start']
            self.queue_path(destination)

    def queue_path(self, destination):
        path = self.find_path(self.car_position, destination)
        self.queued_path = path

    def nearest_passenger(self):
        if self.location_passenger_map:
            came_from, end = self.bfs(self.car_position, lambda current: current in self.location_passenger_map)
            return self.location_passenger_map[end]
        else:
            return None


    def bfs(self, start, break_func=None):
        # break_func should be a function that accepts one argument, the current node
        # and returns a boolean for whether the bfs should stop
        frontier = collections.deque()
        frontier.append(start)
        came_from = {}
        came_from[start] = None

        while frontier:
            current = frontier.popleft()

            if break_func(current):
                break

            for node in self.grid.neighbors(current):
                if node not in came_from:
                    frontier.append(node)
                    came_from[node] = current

        return came_from, current

    def find_path(self, start, end):
        came_from, _ = self.bfs(start, lambda current: current == end)
        path = [end]
        current = end
        while current != start:
            current = came_from[current]
            if current == start:
                break
            path.append(current)
        return path

n = Navigation(Grid(10, 10), car_position=(0,0))
requests = [
    {'name': 'Jimmy', 'start': (0,1), 'end': (0,4)},
    {'name': 'Allison', 'start': (4,4), 'end': (4,0)}
]
n.advance_time(requests)
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
