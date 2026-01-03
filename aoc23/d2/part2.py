import re

# input = [
#   "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#   "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#   "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#   "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#   "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

with open("./aoc23/d2/data.txt") as f:
  input = f.readlines()

result = 0
verbose = False

for line in input:
  game_id_str, game_stats_line = line.split(":")
  if verbose:
    print(game_id_str)
    print(game_stats_line)
  games_stats: list[str] = game_stats_line.split(";")

  max_red = 0
  max_green = 0
  max_blue = 0

  for game_stat in games_stats:
    for boxes_stats in game_stat.split(","):
      n_boxes = re.search(r"\d+", boxes_stats)
      assert n_boxes
      n_boxes = int(n_boxes.group())
      if re.search("blue", boxes_stats):
        max_blue = max(max_blue, n_boxes)
      elif re.search("green", boxes_stats):
        max_green = max(max_green, n_boxes)
      elif re.search("red", boxes_stats):
        max_red = max(max_red, n_boxes)

  if verbose:
    print(max_blue, max_green, max_red)
  result += max_blue * max_green * max_red


print("Result: ", result)
