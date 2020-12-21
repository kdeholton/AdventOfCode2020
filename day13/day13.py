#!/usr/bin/python3

f = open("input", 'r')
lines = [ line.strip() for line in f ]

curr_time = int(lines[0])
busses = lines[1].split(',')
busses = list(filter(('x').__ne__, busses))
busses = [int(bus) for bus in busses]
busses.sort()
earliest_times = [0] * len(busses)
next_times = [0] * len(busses)

for i, bus in enumerate(busses):
  bus = int(bus)
  if bus % curr_time == 0:
    # We can meet a bus exactly when we arrive
    pass
  time = bus * ((curr_time // bus ) + 1)
  earliest_times[i] = time
  next_times[i] = time - curr_time

idx = next_times.index(min(next_times))
next_bus = busses[idx]
wait_time = next_times[idx]

solution_pt1 = next_bus * wait_time

print(solution_pt1)