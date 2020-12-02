#!/usr/bin/python3

f = open("input", 'r')
lines = [ line.strip() for line in f ]

valid_count_1 = 0
valid_count_2 = 0
for line in lines:
  num, letter, pw = line.split()
  low, high = num.split('-')
  low = int(low)
  high = int(high)
  letter = letter[:-1]
  count = pw.count(letter)
  if(count >= low and count <=high):
    # Valid password ver1
    valid_count_1 += 1

  idx_1 = low-1
  idx_2 = high-1
  if((pw[idx_1] == letter) != (pw[idx_2] == letter)):
    valid_count_2 += 1
print(valid_count_1)
print(valid_count_2)
