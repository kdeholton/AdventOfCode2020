#!/usr/bin/python3

f = open("input", 'r')

num_1V_deltas = 0
num_3V_deltas = 0
prev = 0

lines = [ int(line.strip()) for line in f ]

lines.sort()
lines.append(lines[-1] + 3)
delta_list = []

for v in lines:
  delta = v - prev
  if delta == 3:
    num_3V_deltas += 1
  elif delta == 1:
    num_1V_deltas += 1
  else:
    # Uh oh, we shouldn't have gotten here
    print("SHIT")
  prev = v
  delta_list.append(delta)

prev_v_num = 0
val_list = []
for v in delta_list:
  print(v)
  if v == 1:
    prev_v_num += 1
    continue
  if prev_v_num == 1:
    val_list.append(1)
  elif prev_v_num == 2:
    val_list.append(2)
  elif prev_v_num == 3:
    val_list.append(4)
  elif prev_v_num == 4:
    val_list.append(7)
  elif prev_v_num == 0:
    pass
  else:
    print("Uh oh")
  prev_v_num = 0

print(val_list)
final_product = 1
for v in val_list:
  final_product *= v

print("1V deltas: {}".format(num_1V_deltas))
print("3V deltas: {}".format(num_3V_deltas))
print("Product: {}".format(num_1V_deltas * num_3V_deltas))
print("Final Product: {}".format(final_product))
