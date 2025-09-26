import itertools
import os
import pickle
import networkx as nx
from functools import cache

D = ((1, 0), (-1, 0), (0, 1), (0, -1))

path_cache = dict()


@cache
def min_len_sequence(a: tuple, remaining_herbs: tuple, b: tuple) -> int:
  if not remaining_herbs:
    return nx.shortest_path_length(G, a, b)
  next_herb = remaining_herbs[0]
  len_min = float("inf")
  for next_pos in targets[next_herb]:
    if (a, next_pos) in path_cache:
      length = path_cache[(a, next_pos)]
    else:
      length = nx.shortest_path_length(G, a, next_pos)
      path_cache[(a, next_pos)] = length
      path_cache[(next_pos, a)] = length
    if length >= len_min:
      continue
    length += min_len_sequence(next_pos, remaining_herbs[1:], b)
    len_min = min(len_min, length)
  return len_min


part1 = 0
# with open(f"input1.txt", "r") as f: notes = f.read()
# notes = notes.split("\n")
# grid = {(r, c): s for r, row in enumerate(notes) for c, s in enumerate(row) if s != "#"}
# start = min(grid)     # (0, notes[0].index("."))
# targets = {k for k, v in grid.items() if v == "H"}
#
# edges = set()
# for r, c in grid:
#   for dr, dc in D:
#     n_pos = (r+dr, c+dc)
#     if n_pos in grid: edges.add(((r,c), n_pos))
#
# G = nx.Graph()
# G.add_edges_from(edges)
# part1 = min([2 * nx.shortest_path_length(G, source=start, target=t) for t in targets])
print(f"Part   I: {part1}")

part2 = 0
# with open(f"input2.txt", "r") as f: notes = f.read()
# notes = notes.split("\n")
# grid = {(r, c): s for r, row in enumerate(notes) for c, s in enumerate(row) if s not in "#~"}
# start = min(grid)     # (0, notes[0].index("."))
# herbs = {v for k, v in grid.items() if v != "."}
# targets = dict()
# for h in herbs:
#   targets[h] = []
#   for pos, v in grid.items():
#     if v != h: continue
#     targets[h].append(pos)
#
# # any combination of start-(a, b, c)-start
# all_paths = []
# for herb_order in itertools.permutations(herbs, len(herbs)):
#   paths = [[start]]
#   for h in herb_order:
#     len_t = len(targets[h])
#     paths = [p[:] for p in paths for _ in range(len_t)]
#     len_p = len(paths)
#     for i, p in enumerate(paths):
#       p.append(targets[h][i % len_t])
#   for p in paths:
#     p.append(start)
#   all_paths += paths
#
# edges = set()
# for r, c in grid:
#   for dr, dc in D:
#     n_pos = (r+dr, c+dc)
#     if n_pos in grid: edges.add(((r,c), n_pos))
#
# G = nx.Graph()
# G.add_edges_from(edges)
# cache = dict()
# part2 = float("inf")
# for path in all_paths:
#   len_p = 0
#   for start, target in itertools.pairwise(path):
#     if (start, target) in cache:
#       d_len_p = cache[(start, target)]
#     elif (target, start) in cache:
#       d_len_p = cache[(target, start)]
#     else:
#       d_len_p = nx.shortest_path_length(G, source=start, target=target)
#       cache[(start, target)] = d_len_p
#       cache[(target, start)] = d_len_p
#     len_p += d_len_p
#     if len_p > part2:
#       break
#   part2 = min(part2, len_p)
print(f"Part  II: {part2}")

part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
notes = notes.split("\n")
grid = {(r, c): s for r, row in enumerate(notes) for c, s in enumerate(row) if s not in "#~"}

edges = set()
for r, c in grid:
  for dr, dc in D:
    if (n_pos := r + dr, c + dc) in grid: edges.add(((r, c), n_pos))

G = nx.Graph()
G.add_edges_from(edges)

start = min(grid)
herbs = sorted(list({v for k, v in grid.items() if v != "."}))
targets = {h: [pos for pos, v in grid.items() if v == h] for h in herbs}

bases = [max(targets["E"]), start, min(targets["R"])]
areas = ["ABCDE", "EGHIJKR", "NOPQR"]

for base, area in zip(bases, areas):
  print(base, area)
  len_min = float("inf")
  sequences = list(itertools.permutations(area))
  for sequence in sequences:
    length = min_len_sequence(base, sequence, base)
    len_min = min(len_min, length)
  part3 += len_min
print(f"Part III: {part3}")
# 400 len: NOK, 1st: NOK
