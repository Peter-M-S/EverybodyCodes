from collections import deque
import networkx as nx

DRDC = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_grid(notes):
  grid = {(r, c): s for r, line in enumerate(notes.split("\n")) for c, s in enumerate(line) if s != "#"}
  palms = {pos for pos in grid if grid[pos] == "P"}
  start = [(r, c) for r, c in grid if
           (r == 0 or r + 1 == len(notes.split("\n"))) or
           (c == 0 or c + 1 == len(notes.split("\n")[0]))
           ]
  return grid, palms, start


def get_graph(grid):
  G = nx.Graph()
  G.add_nodes_from(grid.keys())
  for n0 in G.nodes:
    for dr, dc in DRDC:
      n1 = (n0[0] + dr, n0[1] + dc)
      if n1 in grid:
        G.add_edge(n0, n1)
  return G


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
grid, palms, start = get_grid(notes)
G = get_graph(grid)

part1 = max([nx.shortest_path_length(G,start[0], p) for p in palms])
print(f"Part   I: {part1}")


part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
grid, palms, start = get_grid(notes)
G = get_graph(grid)

dist = {s:dict() for s in start}
for s in start:
  for p in palms:
    dist[s][p] = nx.shortest_path_length(G, s, p)

part2 = max([min([dist[s][p] for s in start]) for p in palms])
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
grid = {(r, c): s for r, line in enumerate(notes.split("\n")) for c, s in enumerate(line) if s != "#"}
palms = {pos for pos in grid if grid[pos] == "P"}
dist = {pos: {p: 0 for p in palms} for pos in grid}

for palm in palms:
  seen = set()
  q = deque([palm])
  while q:
    pos = q.popleft()
    for dr, dc in DRDC:
      n_pos = pos[0]+dr, pos[1]+dc
      if n_pos in seen: continue
      seen.add(n_pos)
      if n_pos in grid:
        q.append(n_pos)
        dist[n_pos][palm] = dist[pos][palm] + 1

part3 = min([sum(v.values()) for k, v in dist.items()])
print(f"Part III: {part3}")
