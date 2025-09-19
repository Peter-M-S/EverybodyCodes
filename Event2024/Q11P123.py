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

populations = dict((c, dict()) for c in converse)
for cat in converse:
  populations[cat][1] = len(converse[cat])

for day in range(2, 21):
  for cat in populations:
    populations[cat][day] = sum([populations[c][day-1] for c in converse[cat]])

populations_20 = [populations[c][20] for c in converse]
part3 = max(populations_20) - min(populations_20)


#   gen = [cat]
#   for day in range(20):
#     next_gen = []
#     for s in gen: next_gen += converse[s]
#     gen = next_gen
#   populations.append(len(gen))
# part3 = max(populations)-min(populations)
print(f"Part III: {part3}")
