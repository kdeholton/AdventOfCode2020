#!/usr/bin/python3




f = open("input", 'r')
#f = open("input_small", 'r')

answer = 0


group = set()
for line in f:
  line = line.strip()
  if (len(line) == 0):
    # End of group
    answer += len(group)
    group = set()
  for c in line:
    group.add(c)

answer += len(group)


print(answer)
