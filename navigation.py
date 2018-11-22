from grid import Grid
import collections

class Navigation:

    def __init__(self, grid):
        self.grid = grid
        self.requests = []

    def advance_time(requests):
        requests = [
            {'name': 'Jimmy', 'start': (0,0), 'end': (1,1)}
        ]

    def bfs(self, start, end):
        frontier = collections.deque()
        frontier.append(start)
        came_from = {}
        came_from[start] = None

        while frontier:
            current = frontier.popleft()

            if current == end:
                break
            # print(current)
            for node in self.grid.neighbors(current):
                if node not in came_from:
                    frontier.append(node)
                    came_from[node] = current

        return came_from

    def get_path(self, start, end):
        came_from = self.bfs(start, end)
        path = []
        current = end
        while current != start:
            current = came_from[current]
            if current == start:
                break
            path.append(current)
        return path

n = Navigation(Grid())
start, end = (0,0), (3,3)

print(n.get_path(start, end))
