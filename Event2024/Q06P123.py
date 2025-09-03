def back_tracking(path: list) -> list:
  last_origin = path[-1]
  if last_origin == "RR": return path
  for k, v in graph.items():
    if k in path: continue
    if last_origin in v: return back_tracking(path + [k])


for part in (1,2,3):
  with open(f"input{part}.txt", "r") as f: notes = f.read()
  graph = dict()
  for line in notes.split("\n"):
    origin, targets = line.split(":")
    graph[origin] = targets.split(",")
  fruit_branches = [["@", k] for k, v in graph.items() if "@" in v]

  fruit_paths = []
  for branch in fruit_branches:
    fruit_paths.append(back_tracking(branch))

  lengths = list(map(len, fruit_paths))
  for i, n in enumerate(lengths):
    if lengths.count(n) > 1: continue
    if part == 1:
      result = "".join(fruit_paths[i][::-1])
    else:
      result = "".join([p[0] for p in fruit_paths[i][::-1]])
    break
  print(f"Part {part}: {result}")
