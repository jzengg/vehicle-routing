# Vehicle Routing
A simplistic representation of vehicle routing in a ride-hailing context.
Some assumptions I made:
  - each passenger has a unique pickup and dropoff location
  - we want to minimize the amount of time a person spends in the car, so we
  only pick up passengers that are directly along the existing route

# Classes

## Grid
The graph like representation of our grid. We can use this class to get neighbors
of a given position, i.e. intersections we can reach from our current position.
These neighbors are validated by `in_bounds` so that they are within the given
dimensions of the grid.

## Car
Only responsible for passengers, including picking passengers up and dropping them off.

## Navigation
This class could be further broken down into additional classes.
It's responsible for advancing time, finding paths, finding the nearest passenger,
and moving the car around.

The meat of the logic happens here. We start by using BFS to greedily find the nearest
passenger to the car's current position. We continue using BFS to take the shortest path to pick the passenger up as well as drop the passenger off.

We made some tradeoffs here in terms of pooling riders efficiently. We'll only pick
up riders that are directly along the way to minimize the time a passenger spends
in the car. Personally, I get carsick easily, so I'd rather wait outside longer than
sit in the car as we make detours to pick up additional riders.

An alternative approach might be to try and pick up riders as often as possible.
We could monitor where the dropoffs for each of our passengers are and set a cap
on how long a passenger should be in the car and how many passengers we'll allow in the car.
We might be able to drop off passengers more efficiently like this since we'll have more options that might be conveniently along the way.

We could also use Djikstra's algorithm with a higher edge weight for edges that touch a passenger or A* with a heuristic like additional passengers near pickup or dropoff.
