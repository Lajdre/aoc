import re

# input = [
#   "two1nine",
#   "eightwothree",
#   "abcone2threexyz",
#   "xtwone3four",
#   "4nineeightseven2",
#   "zoneight234",
#   "7pqrstsixteen",
# ]

with open("aoc23/d1/data.txt") as f:
  input = f.readlines()

total_sum = 0


def match_number(candidate: str):
  if candidate.isdigit():
    return candidate

  if candidate == "one" or candidate == "eno":
    return "1"
  elif candidate == "two" or candidate == "owt":
    return "2"
  elif candidate == "three" or candidate == "eerht":
    return "3"
  elif candidate == "four" or candidate == "ruof":
    return "4"
  elif candidate == "five" or candidate == "evif":
    return "5"
  elif candidate == "six" or candidate == "xis":
    return "6"
  elif candidate == "seven" or candidate == "neves":
    return "7"
  elif candidate == "eight" or candidate == "thgie":
    return "8"
  elif candidate == "nine" or candidate == "enin":
    return "9"
  elif candidate == "zero" or candidate == "orez":
    return "0"

  assert False, candidate


verbose = False
pattern_forward = r"(\d|one|two|three|four|five|six|seven|eight|nine|zero)"
pattern_backward = r"(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez)"
for line in input:
  first = re.search(pattern_forward, line)
  last = re.search(pattern_backward, line[::-1])
  if first and last:
    if verbose:
      print(line)
      print(int(match_number(first.group()) + match_number(last.group())))
    total_sum += int(match_number(first.group()) + match_number(last.group()))

print(total_sum)
