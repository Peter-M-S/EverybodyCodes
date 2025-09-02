with open(f"input1.txt", "r") as f: notes = f.read()

grid = notes.split("\n")
grid = [list(map(int, line.split())) for line in grid]
columns = [list(t) for t in zip(*grid)]
counter = dict()
for i in range(10):
  steps = columns[i % 4].pop(0)
  col = (i + 1) % 4
  length = len(columns[col])
  if steps <= length:
    index = steps - 1
  else:
    index = 2 * length - (steps - 1)

  columns[col].insert(index, steps)
  n = "".join(str(c[0]) for c in columns)
print(f"Part   I: {n}")


with open(f"input2.txt", "r") as f: notes = f.read()

grid = notes.split("\n")
grid = [list(map(int, line.split())) for line in grid]
columns = [list(t) for t in zip(*grid)]
counter = dict()
for i in range(2_000_000):
  steps = columns[i % 4].pop(0)
  col = (i + 1) % 4
  length = len(columns[col])

  if 0 < steps <= length:
    index = steps - 1
  elif length < steps < 2*length:
    index = 2*length-(steps-1)
  else:
    index = 1

  columns[col].insert(index, steps)
  n = "".join(str(c[0]) for c in columns)

  if n in counter:
    counter[n] += 1
  else:
    counter[n] = 1

  if counter[n] == 2024:
    break

print(f"Part  II: {(i+1) * int(n)}")


with open(f"input3.txt", "r") as f: notes = f.read()

grid = notes.split("\n")
grid = [list(map(int, line.split())) for line in grid]
columns = [list(t) for t in zip(*grid)]

seen = {tuple(tuple(c) for c in columns)}
max_shout = "".join(str(c[0]) for c in columns)

for i in range(2_000_000):  # to prevent infinit loop
  claps = columns[i % 4].pop(0)
  col = (i + 1) % 4
  length = len(columns[col])

  steps = claps % (2 * length)
  if 0 < steps <= length:
    index = steps - 1
  elif length < steps < 2 * length:
    index = 2 * length - (steps - 1)
  else:  # claps == 2n * length
    index = 1

  columns[col].insert(index, claps)

  max_shout = max("".join(str(c[0]) for c in columns), max_shout)
  s = tuple(tuple(c) for c in columns)
  if s not in seen:
    seen.add(s)
  else:
    # found state again
    break

print(f"Part III: {max_shout}")
