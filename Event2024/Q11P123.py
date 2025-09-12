part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
converse = dict()
for line in notes.split("\n"):
  k, v = line.split(":")
  converse[k] = v.split(",")

gen = ["A"]
for day in range(4):
  next_gen = []
  for s in gen: next_gen += converse[s]
  gen = next_gen
part1 = len(gen)
print(f"Part   I: {part1}")

part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
converse = dict()
for line in notes.split("\n"):
  k, v = line.split(":")
  converse[k] = v.split(",")

gen = ["Z"]
for day in range(10):
  next_gen = []
  for s in gen: next_gen += converse[s]
  gen = next_gen
part2 = len(gen)

print(f"Part  II: {part2}")

part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
converse = dict()
for line in notes.split("\n"):
  k, v = line.split(":")
  converse[k] = v.split(",")
populations = []
for cat in converse:
  print(cat)
  gen = [cat]
  for day in range(20):
    next_gen = []
    for s in gen: next_gen += converse[s]
    gen = next_gen
  populations.append(len(gen))
part3 = max(populations)-min(populations)
print(f"Part III: {part3}")
