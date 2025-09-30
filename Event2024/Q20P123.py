import itertools

import networkx as nx

DRDC = {(1, 0), (-1, 0), (0, 1), (0, -1)}
delta = {".": -1, "-": -2, "+": 1}
gain = {3: (2, 4), 4: (4, 4)}


def neighbors(pos) -> set:
  r, c = pos
  return {(r+dr, c+dc) for dr, dc in DRDC}


# not needed as shortest path will never step back
def is_valid_path(path) -> bool:
  for n0, n2 in zip(path[:-2], path[2:]):
    if n0 == n2: return False
  return True


def altitude(path, grid, alt_0=0) -> int:
  return alt_0 + sum([delta[grid[n]] for n in path[1:]])


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
grid = {(r, c): s for r, row in enumerate(notes.split("\n")) for c, s in enumerate(row)}
start, downs, ups, obstacles = tuple(), set(), set(), set()
for pos, s in grid.items():
  match s:
    case "#":
      obstacles.add(pos)
    case "S":
      start = pos
      # obstacles.add(pos)
      grid[start] = "."
    case "-":
      downs.add(pos)
    case "+":
      ups.add(pos)
    case _:
      pass
for pos in obstacles: del grid[pos]

best_loops = {i: set() for i in (3, 4)}
# 2-loop: +0 per 4 steps  0%
# 3-loop: +2 per 4 steps  50%
# 4-loop: +4 per 4 steps  100%
# 5-loop: +4 per 6 steps  67%
# 6-loop: +6 per 6 steps  100% (4-loop is subloop of this)
for r, c in ups:
  for drdc in [((0,1), (1,1), (1,0)), ((0,-1), (1,-1), (1,0))]:
    temp = [(r,c)]
    for dr, dc in drdc:
      n_pos = r+dr, c+dc
      if n_pos in ups and n_pos not in downs:
        temp.append(n_pos)
    if len(temp) in (1, 2): continue
    best_loops[len(temp)].add(tuple(sorted(temp)))
# print(best_loops)

G = nx.Graph()
for n0 in grid:
  for n1 in neighbors(n0):
    if n1 in grid: G.add_edge(n0, n1)
# print(G.nodes)

best_pos = dict()
for loop_size in (4, 3):
  for loop in best_loops[loop_size]:
    best_pos[loop] = dict()
    for pos in loop:
      best_altitude, best_path = 0, []
      all_shorts = nx.all_shortest_paths(G, start, pos)
      for sp in all_shorts:
        a = altitude(sp, grid, 1000)
        if a > best_altitude: best_path, best_altitude = sp, a
      best_pos[loop][pos] = best_altitude, len(best_path)-1

for k,v in best_pos.items():
  print(k,v)

a_max = 0
for loop,v in best_pos.items():
  da, dt = gain[len(loop)]
  for pos, (ba, t) in v.items():
    time = 100 - t
    full, part = divmod(time, dt)
    a_max = max(a_max, ba + full*da + part)
    print(a_max)

part1 = a_max
print(f"Part   I: {part1}")

part2 = 0 
with open(f"input2.txt", "r") as f: notes = f.read()

print(f"Part  II: {part2}")

part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()

print(f"Part III: {part3}")
