from enum import Enum

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(str(node))
      node = node.next
    nodes.append("None")
    return "\n".join(nodes)

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def get_head(self):
    return self.head

  def succeeded_building_logical_list(self):
    node = self.head
    infinite_loop = False
    accumulator = 0
    while node is not None:
      next_instr = 1
      if node.visited:
        print("INFINTE LOOP")
        infinite_loop = True
        break
      if node.instruction == Instr.NOP:
        pass
      elif node.instruction == Instr.ACC:
        accumulator += int(node.value)
      elif node.instruction == Instr.JMP:
        next_instr = int(node.value)

      node.visited = True

      dir_forward = True
      if next_instr < 0:
        dir_forward = False
        next_instr *= -1

      while next_instr != 0:
        if dir_forward:
          node = node.next
        else:
          node = node.previous
        next_instr -= 1

    print("Accumulator value: {}".format(accumulator))
    return not infinite_loop

  def has_infinite_loop(self):
    node = self.head
    while node is not None:
      if node.visited:
        return True
      node.visited = True
      node = node.nextInstruction
    return False

  def reset_visit_count(self):
    for node in self:
      node.visited = False

  def insert_at_end(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      old_tail = self.tail
      self.tail = node
      old_tail.next = node
      node.previous = old_tail

  def merge_adjacent(self, node, other):
    if node.next is not other and other.next is not node:
      return False
    if node.instruction != other.instruction:
      return False
    first = None
    last = None 
    if node.next is other:
      first = node
      last = other
    else:
      first = other
      last = node

    first.next = last.next
    first.next.previous = first
    last.next = None
    last.previous = None
    first.value += last.value
    return True


class Instr(Enum):
  NOP = 0
  ACC = 1
  JMP = 2

class Instruction:
  def __init__(self, instruction, value):
    self.instruction = instruction
    self.value = value

class Node:
  def __init__(self, data):
    self.instruction = data['instruction']
    self.value = data['value']
    self.below = None
    self.next = None
    self.previous = None
    self.visited = False
    self.nextInstruction = None

  def __repr__(self):
    return "{}: {}".format(self.instruction, self.value)

  def swap_type(self):
    if self.instruction == Instr.NOP:
      self.instruction = Instr.JMP
    elif self.instruction == Instr.JMP:
      self.instruction = Instr.NOP