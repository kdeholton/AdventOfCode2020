#!/usr/bin/python3

from waiting_room import *

f = open("input", 'r')
lines = [ line.strip() for line in f ]

width = len(lines[0])
height = len(lines)

waiting_room = WaitingRoom(width, height)

for y, line in enumerate(lines):
  for x, seat in enumerate(line):
    if seat == "L":
      waiting_room.initSeat(x, y)

while(waiting_room.iterateStepPart2()):
  pass

print(waiting_room)
print(waiting_room.numOccupied())