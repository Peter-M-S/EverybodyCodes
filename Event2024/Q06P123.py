part = 1
with open(f"input1.txt", "r") as f: notes = f.read()
graph = dict()
for line in notes.split("\n"):
  origin, targets = line.split(":")
  graph[origin] = targets.split(",")
paths = list()


def explore(path: list) -> None:
  last_target = path[-1]
  if last_target == "@":
    paths.append(path)
    return

  if last_target not in graph: return

  for target in graph[last_target]:
    explore(path + [target])


start = "RR"
explore([start])
lengths = list(map(len, paths))
for i, n in enumerate(lengths):
  if lengths.count(n) > 1: continue
  part = "".join(paths[i])
  break

print(f"Part   I: {part}")

part = 2
with open(f"input2.txt", "r") as f: notes = f.read()
graph = dict()
for line in notes.split("\n"):
  origin, targets = line.split(":")
  graph[origin] = targets.split(",")
fruit_branches = [["@", k] for k, v in graph.items() if "@" in v]


def back_tracking(path: list) -> list:
  last_origin = path[-1]
  if last_origin == "RR":
    return path
  for k, v in graph.items():
    if k in path: continue
    if last_origin in v:
      return back_tracking(path + [k])
  return []


fruit_paths = []
for branch in fruit_branches:
  fruit_paths.append(back_tracking(branch))

lengths = list(map(len, fruit_paths))
for i, n in enumerate(lengths):
  if lengths.count(n) > 1: continue
  part = "".join([p[0] for p in fruit_paths[i][::-1]])
  break

print(f"Part  II: {part}")


part = 3
with open(f"input3.txt", "r") as f: notes = f.read()
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
  part = "".join([p[0] for p in fruit_paths[i][::-1]])
  break

print(f"Part III: {part}")
