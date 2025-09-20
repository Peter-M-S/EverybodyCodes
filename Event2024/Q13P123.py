import networkx as nx

DRDC = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DELTAS = [0,1,2,3,4,5,4,3,2,1]


def get_maze(notes) -> tuple:
  notes = notes.split("\n")
  maze, starts, target = dict(), list(), tuple()
  for r, row in enumerate(notes):
    for c, s in enumerate(row):
      if s in "# ": continue
      if s == "S": starts, s = starts+[(r, c)], "0"
      elif s == "E": target, s = (r, c), "0"
      maze[(r, c)] = int(s)
  return maze, starts, target


def get_options(maze: dict, r: int, c: int) -> list:
  return [(r + dr,c + dc) for dr, dc in DRDC if (r + dr,c + dc) in maze]


def weight(a: int, b: int) -> int:
  return 1 + (DELTAS[-a:] + DELTAS[:-a])[b]


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
maze, starts, target = get_maze(notes)
start = starts[0]
edges = {(a, b) for a in maze for b in get_options(maze, *a)}

G = nx.Graph()
G.add_nodes_from(maze)
G.add_weighted_edges_from([(a, b, weight(maze[a], maze[b])) for a,b in edges])
path = nx.shortest_path(G, source=start, target=target, weight='weight')

part1 = sum([weight(maze[a], maze[b]) for a, b in zip(path[:-1], path[1:])])
print(f"Part   I: {part1}")


part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
maze, starts, target = get_maze(notes)
start = starts[0]
edges = {(a, b) for a in maze for b in get_options(maze, *a)}

G = nx.Graph()
G.add_nodes_from(maze)
G.add_weighted_edges_from([(a, b, weight(maze[a], maze[b])) for a,b in edges])
path = nx.shortest_path(G, source=start, target=target, weight='weight')

part2 = sum([weight(maze[a], maze[b]) for a, b in zip(path[:-1], path[1:])])
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
maze, starts, target = get_maze(notes)
edges = {(a, b) for a in maze for b in get_options(maze, *a)}

G = nx.Graph()
G.add_nodes_from(maze)
G.add_weighted_edges_from([(a, b, weight(maze[a], maze[b])) for a,b in edges])
paths = nx.shortest_path(G, source=None, target=target, weight='weight')

part3 = float('inf')
for k, v in paths.items():
  if k in starts:
    part3 = min(part3, sum([weight(maze[a], maze[b]) for a, b in zip(v[:-1], v[1:])]))
print(f"Part III: {part3}")
