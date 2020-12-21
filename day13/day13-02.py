#!/usr/bin/python3
import numpy as np

f = open("input", 'r')
lines = [ line.strip() for line in f ]

curr_time = int(lines[0])
busses = lines[1].split(',')
busses_int = [int(bus) for bus in list(filter(('x').__ne__, busses))]

deltas = []
for i, bus in enumerate(busses):
  if bus != 'x':
    deltas.append(int(i))

wraparound_t = np.lcm.reduce(busses_int)

t = 0
increment_amt = 1
hightest_idx = -1
while t < wraparound_t:
  solution = True
  for delta_idx, bus in enumerate(busses_int):
    delta = deltas[delta_idx]
    if (t+delta) % bus != 0:
      solution = False
      break
    else:
      if delta_idx > hightest_idx:
        hightest_idx = delta_idx
        increment_amt *= bus

  if solution:
    print(t)
    break
  t += increment_amt