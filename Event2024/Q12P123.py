def get_arrays(notes: str) -> tuple:
  grid = notes.split("\n")[::-1]
  segments, targets, hardrocks = dict(), set(), set()
  for r, row in enumerate(grid):
    for c, s in enumerate(row):
      if s in "ABC":
        segments[s] = (r, c)
      elif s == "T":
        targets.add((r, c))
      elif s == "H":
        targets.add((r, c))
        hardrocks.add((r, c))
  return segments, targets, hardrocks


def trajectory(pos: tuple, power: int) -> list:
  (r, c), tr = pos, list()
  for p in range(power):  # ascend
    r += 1
    c += 1
    tr.append((r, c))
  for p in range(power):  # horizontal (r remains)
    c += 1
    tr.append((r, c))
  while r > 0:  # descend
    r -= 1
    c += 1
    tr.append((r, c))
  return tr


def ranking(pos: tuple, power: int) -> int:
  return pos[0] * power


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
segments, targets, hardrocks = get_arrays(notes)

while targets:
  rank_min, best_shot = float("inf"), (None, None, None)
  d_min = min(targets, key=lambda x: x[1])[1]
  d_max = max(targets, key=lambda x: x[1])[1]
  p_min = max(int(d_min / 3) - 3, 1)
  p_max = int(d_max / 3) + 4
  for s, pos in segments.items():
    for p in range(p_min, p_max):
      tr = trajectory(pos, p)
      if targets & set(tr):
        r = ranking(pos, p)
        if r < rank_min:
          rank_min, best_shot = r, (pos, p, targets & set(tr))
  targets -= best_shot[2]
  part1 += rank_min
print(f"Part   I: {part1}")

part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
segments, targets, hardrocks = get_arrays(notes)

while targets:
  rank_min, best_shot = float("inf"), (None, None, None)
  d_min = min(targets, key=lambda x: x[1])[1]
  d_max = max(targets, key=lambda x: x[1])[1]
  p_min = max(int(d_min / 3) - 3, 1)
  p_max = int(d_max / 3) + 7  # finding by trial and error
  for s, pos in segments.items():
    for p in range(p_min, p_max):
      tr = trajectory(pos, p)
      hit = tuple()
      while targets & set(tr):
        hit = tr.pop()
      if hit:
        r = ranking(pos, p)
        if r < rank_min:
          rank_min, best_shot = r, (pos, p, hit)
  if best_shot[2] is None or len(best_shot[2]) == 0:
    print(f"no hit with {best_shot[0]} * power {best_shot[1]}")
    a = input()
    continue
  if best_shot[2] in hardrocks:
    hardrocks -= {best_shot[2]}
    part2 += rank_min
  targets -= {best_shot[2]}
  part2 += rank_min
print(f"Part  II: {part2}")


part3 = 0
# solved only with help from reddit -> github/mmdoogie
with open(f"input3.txt", "r") as f: notes = f.read()
meteors = []
for line in notes.split("\n"):
  c0, r0 = tuple(map(int, line.split()))  # col , row relative to pos("A")  = (0, 0)
  meteors.append((r0, c0))


def ranking_of_location(mr, mc) -> int:  # row, col -> segment_n * power
  # calculate for different cases of positions or areas
  if (mr, mc) == (3, 2):  # One weird case:  "C"=3*1 < "B"=2*2
    c, p = 3, 1
  elif mc <= mr:  # col <= row -> meteor is above or on x=y
    # -> use the catapult in this line, hit on ascent -> min power = distance to column = col
    # e.g. mr=2, mc=1 use catapult "B"
    c, p = (mr - mc) + 1, mc  # (mr-mc): segment-to-use index, +1 is value
  elif mr > mc // 2:
    # row > col//2 -> positions below x=y where A is best ranking of alternatives
    c, p = 1, mr
  else:  # other cases have only one single setting, in each row, every 3rd position by same catapult
    p, c = divmod(mr + mc, 3)  # divmod(a, b) = a//b, a%b
    c = c + 1
  return c * p


for meteor in meteors:
  mr, mc = meteor  # i=y=row, j=x=col
  time = (mc + 1) // 2  # half distance to left = hit position
  # mc is odd: mc // 2 = n, (mc+1)//2 = n+1
  # -> time from start to hit is one step longer than target to hit, catapult can start one step later (OK)
  # mc is even: # mc// 2 = n, (mc+1)//2  = n
  mr -= time
  mc -= time
  # (mr. mc) = hit position
  part3 += ranking_of_location(mr, mc)

print(f"Part III: {part3}")
