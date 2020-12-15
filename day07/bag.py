from collections import defaultdict
import re

class Bag:
  all_bags = {}

  @classmethod
  def create(cls, color):
    if color not in Bag.all_bags:
      new_bag = Bag(color)
      Bag.all_bags[color] = new_bag
      return new_bag
    else:
      return Bag.all_bags[color]

  def __eq__(self, other):
    return self.color == other.color

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash(self.color)

  def __init__(self, color):
    assert color not in Bag.all_bags
    self.color = color
    self.children = defaultdict(None)
    self.parents = defaultdict(None)

  def add_parent(self, parent, num):
    assert parent not in self.parents
    self.parents[parent] = int(num)

  def add_child(self, child, num):
    assert child not in self.children
    self.children[child] = int(num)
    child.add_parent(self, num)

  def get_num_bags_below(self):
    sum = 0
    for child in self.children:
      sum += self.children[child] * (1 + (child.get_num_bags_below()))
    return sum

  def get_possible_containing_bags(self):
    result = set()
    for parent in self.parents:
      result.add(parent)
      result = result.union(parent.get_possible_containing_bags())
    return result

  def __str__(self):
    return self.color

  def __repr__(self):
    return self.__str__()
