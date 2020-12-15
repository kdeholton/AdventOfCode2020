#!/usr/bin/python3

f = open("input", 'r')
lines = [ list(line.strip()) for line in f ]

pos = {}
pos['x'] = 0
pos['y'] = 0
X_MAX = len(lines[0])
Y_MAX = len(lines)

tree_count = 0

def count_tree(pos):
  global tree_count
  row = pos['y']
  col = pos['x']
  if lines[row][col] == '#':
    tree_count += 1

def increment_pos(pos, addl_x, addl_y):
  pos['y'] = pos['y'] + addl_y
  pos['x'] = (pos['x'] + addl_x) % X_MAX

def reset(pos):
  global tree_count
  tree_count = 0
  pos['x'] = 0
  pos['y'] = 0

# (x, y)
slope_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]

product = 1
result_list = []
for addl_x, addl_y in slope_list:
  while (pos['y'] < Y_MAX):
    count_tree(pos)
    increment_pos(pos, addl_x, addl_y)
  print("Slope of x={}, y={} has tree count of {}".format(addl_x, addl_y, tree_count))
  product = product * tree_count
  reset(pos)

print(product)
