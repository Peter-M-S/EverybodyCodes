from itertools import cycle

DRDC = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1)]


def rotate(pos, grid, rot) -> dict:
  r, c = pos
  FRFC = DRDC[1:] + DRDC[:1] if rot == "L" else DRDC[-1:] + DRDC[:-1]
  new_grid = grid.copy()
  for (dr, dc), (fr, fc) in zip(DRDC, FRFC):
    new_grid[(r + dr, c + dc)] = grid[r + fr, c + fc]
  return new_grid


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
seq, lines = notes.split("\n\n")
lines = lines.split("\n")
grid = {(r, c): s for r, row in enumerate(lines) for c, s in enumerate(row)}

rotation_points = [(r, c) for (r, c) in grid if
                   r != 0 and r != len(lines) - 1 and
                   c != 0 and c != len(lines[0]) - 1]
rotation_points.sort()

for pos, rotor in zip(rotation_points, seq*len(rotation_points)):
  grid = rotate(pos, grid, rotor)

part1 = "".join([grid[pos] for pos in sorted(grid) if grid[pos].isdigit()])
print(f"Part   I: {part1}")


part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
# with open(f"example2.txt", "r") as f: notes = f.read()
seq, lines = notes.split("\n\n")
lines = lines.splitlines()
grid = {(r, c): s for r, row in enumerate(lines) for c, s in enumerate(row)}
rows, cols = len(lines), len(lines[0])
rotation_points = [(r, c) for (r, c) in grid if
                   r != 0 and r != len(lines) - 1 and
                   c != 0 and c != len(lines[0]) - 1]
rotation_points.sort()

n = 100
# # to zip rotations_points*n times and seq*len(rotation_points)
# # did not work, as for each round (starting at rotation_point (1, 1))
# # also STARTS WITH the BEGINNING of seq, not continue from last seq-position
# # this did not make a difference in part1 and example!
# rotation_points *= n
# for pos, rot in zip(rotation_points, seq*len(rotation_points)):
#   grid = rotate(pos, grid, rot)
for i in range(n):
  for pos, rot in zip(rotation_points, seq*len(rotation_points)):
    grid = rotate(pos, grid, rot)

for r in range(rows):
  line = "".join([grid[(r, c)] for c in range(cols)])
  if ">" in line and "<" in line:
    part2 = line[line.index(">")+1:line.index("<")]
  print("".join([grid[(r, c)] for c in range(cols)]))
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()

print(f"Part III: {part3}")
