#!/usr/bin/python3
import sys

def parse_seat(seat):
  def recurse(string, low, high):
    mid = (low+high)//2
    if (len(string) == 1):
      return low if string == 'L' else high
    if string[0] == 'L':
      return recurse(string[1:], low, mid)
    else:
      return recurse(string[1:], mid+1, high)

  row_str = seat[:-3].replace('B', 'H').replace('F', 'L')
  col_str = seat[-3:].replace('R', 'H').replace('L', 'L')
  row = recurse(row_str, 0, 127)
  col = recurse(col_str, 0, 7)

  row_id = row*8 + col
  return row_id

def missing_number(lowest_id, highest_id, current_sum, n):
  return ((lowest_id + highest_id) / 2 * (n+1) - current_sum)

if(__name__ == "__main__"):
  f = open("input", 'r')

  highest_row_id = 0
  lowest_row_id = sys.maxsize
  num_ids = 0
  sum_ids = 0

  for line in f:
    line = line.strip()
    row_id = parse_seat(line)
    num_ids += 1
    sum_ids += row_id
    if row_id > highest_row_id:
      highest_row_id = row_id
    if row_id < lowest_row_id:
      lowest_row_id = row_id

  missing_seat_id = missing_number(lowest_row_id, highest_row_id, sum_ids, num_ids)

  print("Highest seat ID: {}".format(highest_row_id))
  print("Missing seat ID: {}".format(int(missing_seat_id)))
