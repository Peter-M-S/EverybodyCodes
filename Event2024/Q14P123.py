import networkx as nx

part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
notes, h = notes.split(","), 0
for s in notes:
  if s.startswith("U"): h += int(s[1:])
  elif s.startswith("D"): h -= int(s[1:])
  part1 = max(part1, h)

print(f"Part   I: {part1}")


part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
plans = notes.split("\n")
D = {"U": (1, 0, 0), "D": (-1, 0, 0), "R": (0, 1, 0), "L": (0, -1, 0), "F": (0, 0, 1), "B": (0, 0, -1)}
uniques = set()
for plan in plans:
  h = c = r = 0
  for s in plan.split(","):
    dh, dc, dr = D[s[0]]
    for i in range(int(s[1:])):
      h, c, r = h + dh, c + dc, r + dr
      uniques.add((h, c, r))

part2 = len(uniques)
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
plans = notes.split("\n")
uniques, trunk, leaves = set(), set(), set()
for plan in plans:
  h = c = r = 0
  for s in plan.split(","):
    dh, dc, dr = D[s[0]]
    for i in range(int(s[1:])):
      h, c, r = h + dh, c + dc, r + dr
      uniques.add((h, c, r))
      if c == r == 0: trunk.add((h, c, r))
  leaves.add((h,c,r))

# use just manhattan distance: does not work for 2nd example and for notes3
edges = set()
for h, c, r in uniques:
  for dh, dc, dr in D.values():
    n_node = (h+dh, c+dc, r+dr)
    if n_node in uniques: edges.add(((h,c,r), n_node))
G = nx.Graph()
G.add_edges_from(edges)

part3 = float("inf")
for start in trunk:
  murk = 0
  for target in leaves:
    murk += nx.shortest_path_length(G, source=start, target=target)-1
  part3 = min(part3, murk)
print(f"Part III: {part3}")
