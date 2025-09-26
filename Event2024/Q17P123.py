import networkx as nx


def add_weighted_edges(G: nx.Graph, part3=False) -> nx.Graph:
  for n0 in G.nodes:
    for n1 in G.nodes:
      if n0 == n1 or (n0, n1) in G.edges: continue
      d = abs(n1[0] - n0[0]) + abs(n1[1] - n0[1])
      if not part3 or (part3 and d < 6): G.add_edge(n0, n1, weight=d)
  return G


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
nodes = {(c + 1, r + 1) for r, line in enumerate(notes.split("\n")[::-1]) for c, s in enumerate(line) if s == "*"}
G = nx.Graph()
G.add_nodes_from(nodes)
G = add_weighted_edges(G)
mst = nx.minimum_spanning_tree(G)
part1 = sum([mst.get_edge_data(*e)["weight"] for e in mst.edges]) + len(mst.nodes)
print(f"Part   I: {part1}")

part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
nodes = {(c + 1, r + 1) for r, line in enumerate(notes.split("\n")[::-1]) for c, s in enumerate(line) if s == "*"}
G = nx.Graph()
G.add_nodes_from(nodes)
G = add_weighted_edges(G)
mst = nx.minimum_spanning_tree(G)
part2 = sum([mst.get_edge_data(*e)["weight"] for e in mst.edges]) + len(mst.nodes)
print(f"Part  II: {part2}")

part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
nodes = {(c + 1, r + 1) for r, line in enumerate(notes.split("\n")[::-1]) for c, s in enumerate(line) if s == "*"}
G = nx.Graph()
G.add_nodes_from(nodes)
G = add_weighted_edges(G, part3=True)

constellations, remaining_nodes, seen = [], set(G.nodes), set()
while remaining_nodes:
  constellation = {min(remaining_nodes)}
  remaining_nodes -= constellation
  growing, checked = True, set()
  while growing:
    growing = False
    for n0 in constellation:
      if n0 in checked: continue
      checked.add(n0)
      if additional_nodes := set(G[n0]) - constellation:
        growing = True
        remaining_nodes -= additional_nodes
        break
    constellation = set(G.nodes) - seen - remaining_nodes
  seen |= constellation
  constellations.append(constellation)
  if len(constellations) > 3:
    constellations = sorted(constellations, key=lambda x: len(x))[-3:]

part3 = 1
for constellation in constellations:
  C = nx.subgraph(G, constellation)
  mst = nx.minimum_spanning_tree(C)
  part3 *= sum([mst.get_edge_data(*e)["weight"] for e in mst.edges]) + len(mst.nodes)

print(f"Part III: {part3}")  # takes quite looong
