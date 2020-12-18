#!/usr/bin/python3
from ship import *

f = open("input", 'r')

ship = Ship()
ship2 = Ship()
for line in f:
  line = line.strip()
  direction = line[0]
  num = int(line[1:])
  if direction == 'N':
    ship.goNorth(num)
    ship2.waypointNorth(num)
  elif direction == 'S':
    ship.goSouth(num)
    ship2.waypointSouth(num)
  elif direction == 'E':
    ship.goEast(num)
    ship2.waypointEast(num)
  elif direction == 'W':
    ship.goWest(num)
    ship2.waypointWest(num)

  elif direction == 'L':
    ship.turnLeft(num)
    ship2.waypointLeft(num)
  elif direction == 'R':
    ship.turnRight(num)
    ship2.waypointRight(num)
  elif direction == 'F':
    ship.goForward(num)
    ship2.goToWaypoint(num)
  


print(ship)
print(ship.manhattanDistanceFromOrigin())
print(ship2)
print(ship2.manhattanDistanceFromOrigin())