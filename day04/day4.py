#!/usr/bin/python3
from collections import defaultdict
import string

f = open("input", 'r')


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def valid_fields(passport):
  for key in required_fields:
    if passport[key] == None:
      return False
  return True


def valid_year(year, min, max):
  return len(year) == 4 and int(year) >= min and int(year) <= max

def valid_hgt(hgt):
  if len(hgt) < 2:
    return False
  ending = hgt[-2:]
  if ending not in ['in', 'cm']:
    return False
  value = hgt[:-2]
  if ending == 'in':
    return int(value) >= 59 and int(value) <= 76
  if ending == 'cm':
    return int(value) >= 150 and int(value) <=193
  return False

def valid_hcl(hcl):
  if len(hcl) != 7:
    return False
  if hcl[0] != '#':
    return false
  num = hcl[1:]
  hex_digits = set(string.hexdigits)
  return all(c in hex_digits for c in num)

def valid_ecl(ecl):
  valid_cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  return ecl in valid_cols

def valid_pid(pid):
  return len(pid) == 9 and pid.isnumeric()

def valid_passport(passport):
  if (not valid_fields(passport)):
    return False
  if not valid_year(passport['byr'], 1920, 2002):
    return False
  if not valid_year(passport['iyr'], 2010, 2020):
    return False
  if not valid_year(passport['eyr'], 2020, 2030):
    return False
  if not valid_hgt(passport['hgt']):
    return False
  if not valid_hcl(passport['hcl']):
    return False
  if not valid_ecl(passport['ecl']):
    return False
  if not valid_pid(passport['pid']):
    return False
  return True


valid_passport_count = 0
passport = defaultdict(lambda: None)
for line in f:
  line = line.strip()

  if(len(line) == 0):
    if (valid_passport(passport)):
      # Validate the previous passport, if it exists
      valid_passport_count += 1
    # new passport
    passport = defaultdict(lambda: None)

  for item in line.split():
    key, value = item.split(":")
    passport[str(key)] = str(value)

if (valid_passport(passport)):
  valid_passport_count += 1

print(valid_passport_count)
