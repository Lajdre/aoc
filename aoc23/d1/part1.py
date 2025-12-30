import re

# input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
with open("aoc23/d1/data.txt") as f:
  input = f.readlines()

total_sum = 0

for line in input:
  first = re.search(r"\d", line)
  last = re.search(r"\d", line[::-1])
  if first and last:
    total_sum += int(first.group() + last.group())

print(total_sum)
