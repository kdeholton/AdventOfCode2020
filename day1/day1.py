#!/usr/bin/python3

f = open("day1.in", 'r')
lines = [int(line.strip()) for line in f]
lines.sort()
desired_vals = [2020-line for line in lines]
result_list = list(set(lines) & set(desired_vals))
if (len(result_list) == 2):
  print("Two values are {} and {}, with sum of {} and product of {}".format(result_list[0], result_list[1], result_list[0] + result_list[1], result_list[0] * result_list[1]))

# Brute force the 3-case
def loop(lines):
  for i in lines:
    for j in lines:
      for k in lines:
        if (2020 == i+j+k):
          print("Three values are {} and {} and {}, with sum of {} and product of {}".format(i, j, k, i+j+k, i*j*k))
          return

loop(lines)
