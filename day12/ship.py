from enum import IntEnum

class Ship:

  class Direction(IntEnum):
    MIN = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    MAX = 5

  def __init__(self):
    self.direction = Ship.Direction.EAST
    self.x = 0
    self.y = 0
    self.waypointX = 10
    self.waypointY = 1

  def goNorth(self,num):
    self.y += num
  def goSouth(self, num):
    self.y -= num
  def goEast(self, num):
    self.x += num
  def goWest(self, num):
    self.x -= num

  def goForward(self, num):
    if self.direction == Ship.Direction.EAST:
      self.goEast(num)
    elif self.direction == Ship.Direction.WEST:
      self.goWest(num)
    elif self.direction == Ship.Direction.NORTH:
      self.goNorth(num)
    elif self.direction == Ship.Direction.SOUTH:
      self.goSouth(num)

  
  def turnLeftOne(self):
    self.direction -= 1
    if self.direction == Ship.Direction.MIN:
      self.direction = Ship.Direction.WEST

  def turnRightOne(self):
    self.direction += 1
    if self.direction == Ship.Direction.MAX:
      self.direction = Ship.Direction.NORTH

  def turnLeft(self, num):
    if num % 90 != 0:
      print("Going left {}: This ain't gon' work".format(num))
    while (num > 0):
      num -= 90
      self.turnLeftOne()

  def turnRight(self, num):
    if num % 90 != 0:
      print("Going right {}: This ain't gon' work".format(num))
    while (num > 0):
      num -= 90
      self.turnRightOne()

  def waypointNorth(self,num):
    self.waypointY += num
  def waypointSouth(self, num):
    self.waypointY -= num
  def waypointEast(self, num):
    self.waypointX += num
  def waypointWest(self, num):
    self.waypointX -= num
  def goToWaypointOne(self):
    self.x += self.waypointX
    self.y += self.waypointY
  def goToWaypoint(self, num):
    while num > 0:
      self.goToWaypointOne()
      num -= 1

  def waypointRightOne(self):
    tempX = self.waypointX
    self.waypointX = self.waypointY
    self.waypointY = -1 * tempX

  def waypointLeftOne(self):
    tempX = self.waypointX
    self.waypointX = -1 * self.waypointY
    self.waypointY = tempX

  def waypointRight(self, num):
    if num % 90 != 0:
      print("Waypoint right {}: This ain't gon' work".format(num))
    while (num > 0):
      num -= 90
      self.waypointRightOne()

  def waypointLeft(self, num):
    if num % 90 != 0:
      print("Waypoint left {}: This ain't gon' work".format(num))
    while (num > 0):
      num -= 90
      self.waypointLeftOne()


  def __repr__(self):
    return "Ship: ({}, {})\nWaypoint: ({}, {})".format(self.x, self.y, self.waypointX, self.waypointY)

  def manhattanDistanceFromOrigin(self):
    return abs(self.x) + abs(self.y)