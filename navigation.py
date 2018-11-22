import collections

from grid import Grid
from car import Car

class Navigation:

    def __init__(self, grid, car_position, car):
        self.grid = grid
        # assume that car starts near center of state, or randomly select a point?
        if car_position is None:
            car_position = (grid.width // 2, grid.height // 2)

        self.car_position = car_position
        self.car = car
        self.location_passenger_map = {}
        self.queued_path = []

    def advance_time(self, requests=None):
        if requests is None:
            requests = []
        for request in requests:
            location = request['start']
            self.location_passenger_map[location] = request

        passengers = self.car.passengers

        if not passengers:
            passenger = self.nearest_passenger()
            if passenger:
                self.navigate_to_passenger(passenger)
            else:
                # could navigate back to middle of map here
                print('no passengers available')
                return

        if self.queued_path:
            new_position = self.queued_path.pop()
            self.move_car(new_position)

        print(self.queued_path)
        print('car is at:', self.car_position)

        # is the current position a pickup or dropoff location
        # assumes that each rider has a distinct pickup and dropoff location
        passenger_to_pickup = self.location_passenger_map.get(self.car_position)
        passenger_to_dropoff = next((p for p in passengers if p['end'] == self.car_position), None)
        if passenger_to_pickup:
            self.location_passenger_map.pop(passenger_to_pickup['start'], None)
            self.pickup_passenger(passenger_to_pickup)
            self.queue_path(self.car_position, passenger_to_pickup['end'])

        if passenger_to_dropoff:
            print('dropped off {}'.format(passenger_to_dropoff['name']))
            self.car.dropoff(passenger_to_dropoff)

        print('\n')

    def move_car(self, position):
        self.car_position = position

    def navigate_to_passenger(self, passenger):
        destination = passenger['start']
        if self.queued_path:
            pickup = self.queued_path[-1]
        else:
            pickup = self.car_position

        self.queue_path(pickup, destination)


    def pickup_passenger(self, passenger):
        print('picking up {}'.format(passenger['name']))
        self.car.pickup(passenger)

    def queue_path(self, pickup, destination):
        path = self.find_path(pickup, destination)
        self.queued_path = path + self.queued_path

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

n = Navigation(Grid(10, 10), car_position=(0,0), car=Car())
requests = [
    {'name': 'Jimmy', 'start': (0,1), 'end': (0,4)},
    {'name': 'Allison', 'start': (0,2), 'end': (4,4)}
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
