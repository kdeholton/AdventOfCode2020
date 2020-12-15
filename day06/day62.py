#!/usr/bin/python3


f = open("input", 'r')
#f = open("input_small", 'r')

answer = 0

def intersection(group):
  result = None
  for g in group:
    if result == None:
      result = g
      continue
    result = list(set(result) & set(g))
  return result


idx = 0
group = []
for line in f:
  line = line.strip()
  if (len(line) == 0):
    # End of group
    intersect = intersection(group)
    ans = len(intersect)
    answer += ans
    group = []
    idx = 0
    continue
  group.append([])
  for c in line:
    group[idx].append(c)
  idx += 1

intersect = intersection(group)
ans = len(intersect)
answer += ans


print(answer)
