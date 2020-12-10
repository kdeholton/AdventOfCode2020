#!/usr/bin/python3
import sys

preamble_len = 25
preamble = []
sums = []
f = open("input", 'r')

def valid_and_insert(num):
  def update_sums(preamble, sums, num):
    sum_list = []
    for n in preamble:
      if n != num:
        sum_list.append(n + num)
    sums.append(sum_list)


  if(len(preamble) < preamble_len):
    preamble.append(num)
    update_sums(preamble, sums, num)
    assert len(sums) == len(preamble)
    return True
  else:
    for sum_list in sums:
      if num in sum_list:
        update_sums(preamble, sums, num)
        preamble.append(num)
        del sums[0]
        del preamble[0]
        assert len(sums) == len(preamble)
        return True
    return False

def find_contiguous(num, f):
  val_list = []
  sum = 0

  f.seek(0)
  for line in f:
    line = int(line.strip())
    sum += line
    val_list.append(line)
    while (sum > num):
      old_val = val_list.pop(0)
      sum -= old_val
    if sum == num:
      if (len(val_list) >= 2):
        print(val_list)
        return max(val_list) + min(val_list)
      else:
        old_val = val_list.pop(0)
        sum -= old_val

bad_value = None
for line in f:
  line = line.strip()
  if not valid_and_insert(int(line)):
    print(line)
    bad_value = int(line)
    break

val = find_contiguous(bad_value, f)
print(val)
