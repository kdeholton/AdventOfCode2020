#!/usr/bin/python3
from bag import *
import re

def parse_rule(rule):
  l, r = rule.split("bags contain")
  l = l.strip()
  r = r.strip().split(',')
  r = [r_val.split(None, 1) for r_val in r]
  r = [[num, re.sub(r'\s*bags?.?$', '', color)] for num,color in r]
  return (l, r)

def add_bag(l, r):
  bag = Bag.create(l)
  for num, child_color in r:
    if num == "no":
      break
    child = Bag.create(child_color)
    bag.add_child(child, num)

if __name__ == '__main__':
  #f = open("input_small", 'r')
  f = open("input", 'r')

  for line in f:
    line = line.strip()
    l, r = parse_rule(line)
    add_bag(l, r)

  my_bag = Bag.create('shiny gold')
  bags_above = my_bag.get_possible_containing_bags()
  print(len(bags_above))

  bags_below = my_bag.get_num_bags_below()
  print(bags_below)