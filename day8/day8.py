#!/usr/bin/python3
from linked_list import *

f = open("input", 'r')
lines = [ line.strip() for line in f ]

linked_list = LinkedList()
for line in lines:
  instr, val = line.split()
  if instr == 'nop':
    instr = Instr.NOP
  elif instr == 'acc':
    instr = Instr.ACC
  elif instr == 'jmp':
    instr = Instr.JMP
  else:
    assert False
  data = {'instruction': instr, 'value': val}
  node = Node(data)
  linked_list.insert_at_end(node)

accumulator = 0
node = linked_list.get_head()

while node is not None:
  if node.instruction != Instr.ACC:
    node.swap_type()
    linked_list.reset_visit_count()
    if not linked_list.succeeded_building_logical_list():
      node.swap_type()
    else:
      # Success!
      print("We did it!")
      break
  node = node.next