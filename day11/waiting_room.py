
class WaitingRoom:

  class Seat:
    def __eq__(self, other):
      return self.x == other.x and self.y == other.y and self.occupied == other.occupied

    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.occupied = False

    def occupy(self):
      self.occupied = True

    def vacate(self):
      self.occupied = False
    
    def isOccupied(self):
      return self.occupied

    def __repr__(self):
      if self.isOccupied():
        return "#"
      else:
        return "L"
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
    # The +2 here is so we don't have to worry about bounds checking at the edge
    self.grid = [ [None]*(height+2) for i in range(width+2)]
    self.grid_next = [ [None]*(height+2) for i in range(width+2)]

  def at(self, x, y):
    return self.grid[x+1][y+1]

  def initSeat(self, x, y):
    self.grid[x+1][y+1] = self.Seat(x,y)
    self.grid_next[x+1][y+1] = self.Seat(x,y)

  def __repr__(self):
    output = ""
    for y in range(self.height):
      for x in range(self.width):
        seat = self.grid[x+1][y+1]
        if seat is None:
          output += "."
        else:
          output += str(seat)
      output += "\n"
    return output

  def numOccupied(self):
    sum = 0
    for x in range(self.width):
      for y in range(self.height):
        seat = self.at(x,y)
        if seat is None:
          continue
        if seat.isOccupied():
          sum += 1
    return sum

  def iterateStepPart1(self):
    has_changed = False
    for y in range(self.height):
      for x in range(self.width):
        seat = self.grid[x+1][y+1]
        if seat is None:
          continue
        num_occupied_adjacent = 0
        for dx in [-1, 0 , 1]:
          for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
              continue
            seat_other = self.grid[x+1+dx][y+1+dy]
            if seat_other is None:
              continue
            if seat_other.isOccupied():
              num_occupied_adjacent += 1
        if seat.isOccupied() and num_occupied_adjacent >= 4:
          self.grid_next[x+1][y+1] = self.Seat(x, y)
          self.grid_next[x+1][y+1].vacate()
        elif not seat.isOccupied() and num_occupied_adjacent == 0:
          self.grid_next[x+1][y+1] = self.Seat(x, y)
          self.grid_next[x+1][y+1].occupy()
        if seat != self.grid_next[x+1][y+1]:
          has_changed = True

    if has_changed:
      for x in range(len(self.grid)):
        for y in range(len(self.grid[0])):
          self.grid[x][y] = self.grid_next[x][y]
    return has_changed

  def checkEmptyRight(self, x, y):
    for dx in range(1, self.width-x):
      seat = self.grid[x+1+dx][y+1]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyLeft(self, x, y):
    for dx in range(1, x+1):
      seat = self.grid[x+1-dx][y+1]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyDown(self, x, y):
    for dy in range(1, self.height-y):
      seat = self.grid[x+1][y+1+dy]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyUp(self, x, y):
    for dy in range(1, y+1):
      seat = self.grid[x+1][y+1-dy]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyDownRight(self, x, y):
    for delta in range(1, min(self.height-y, self.width-x)):
      seat = self.grid[x+1+delta][y+1+delta]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyDownLeft(self, x, y):
    for delta in range(1, min(self.height-y, x+1)):
      seat = self.grid[x+1-delta][y+1+delta]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyUpRight(self, x, y):
    for delta in range(1, min(y+1, self.width-x)):
      seat = self.grid[x+1+delta][y+1-delta]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def checkEmptyUpLeft(self, x, y):
    for delta in range(1, min(y+1, x+1)):
      seat = self.grid[x+1-delta][y+1-delta]
      if seat is None:
        continue
      if seat.isOccupied():
        return True
      else:
        return False
    return False

  def iterateStepPart2(self):
    has_changed = False
    for y in range(self.height):
      for x in range(self.width):
        seat = self.grid[x+1][y+1]
        if seat is None:
          continue
        num_occupied_adjacent = 0


        if self.checkEmptyRight(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyLeft(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyUp(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyDown(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyDownRight(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyUpRight(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyDownLeft(x,y):
          num_occupied_adjacent += 1
        if self.checkEmptyUpLeft(x,y):
          num_occupied_adjacent += 1

        if seat.isOccupied() and num_occupied_adjacent >= 5:
          self.grid_next[x+1][y+1] = self.Seat(x, y)
          self.grid_next[x+1][y+1].vacate()
        elif not seat.isOccupied() and num_occupied_adjacent == 0:
          self.grid_next[x+1][y+1] = self.Seat(x, y)
          self.grid_next[x+1][y+1].occupy()
        if seat != self.grid_next[x+1][y+1]:
          has_changed = True

    if has_changed:
      for x in range(len(self.grid)):
        for y in range(len(self.grid[0])):
          self.grid[x][y] = self.grid_next[x][y]
    return has_changed