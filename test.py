from navigation import Navigation
from grid import Grid
from car import Car

# Some very rudimentary tests that you have to manually check
def setup_navigation(message):
    n = Navigation(Grid(10, 10), car=Car(), car_position=(0,0))
    print(message)
    return n


n = setup_navigation('**Picking up a rider during a ride**')

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

n = setup_navigation('**Pick up the closest rider first**')
requests = [
    {'name': 'Jimmy', 'start': (0,1), 'end': (0,4)},
    {'name': 'Allison', 'start': (8,4), 'end': (4,4)}
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
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()
n.advance_time()

n = setup_navigation('**Receive request while enroute**')

requests = [
    {'name': 'Jimmy', 'start': (0,1), 'end': (0,4)},
]

n.advance_time(requests)
n.advance_time()
n.advance_time()
requests = [
    {'name': 'Allison', 'start': (4,4), 'end': (6,3)}
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
n.advance_time()

n = setup_navigation('**Receive empty request**')
requests = []
n.advance_time()
n.advance_time()
