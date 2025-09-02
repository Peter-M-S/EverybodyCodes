from copy import deepcopy

def digging(n:str):
  with open(f"input{n}.txt", "r") as f: notes = f.read()
  grid = notes.split("\n")
  directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) if n in "12" else ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1),
                                                                     (-1, 1), (1, -1), (1, 1))
  fields = dict()
  for r, row in enumerate(grid):
    for c, s in enumerate(row):
      fields[(r, c)] = 1 if s == "#" else 0

  changed = True
  while changed:
    changed = False
    new_fields = dict()
    for (r,c), depth in fields.items():
      if depth == 0:
        new_fields[(r, c)] = 0
        continue
      neighbors = [fields.get((r+dr, c+dc), 0) for (dr, dc) in directions]
      if all((n_depth == depth) or (n_depth == depth+1) for n_depth in neighbors):
        new_fields[(r, c)] = depth + 1
        changed = True
      else:
        new_fields[(r, c)] = depth
    fields = deepcopy(new_fields)

  return sum(fields.values())


print(f"Part   I: {digging("1")}")
print(f"Part  II: {digging("2")}")
print(f"Part III: {digging("3")}")
