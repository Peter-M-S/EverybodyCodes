with open(f"input1.txt", "r") as f: notes = f.read()
nails = list(map(int,notes.split("\n")))
minimum = min(nails)
total = sum([n-minimum for n in nails])
print(f"Part   I: {total}")

with open(f"input2.txt", "r") as f: notes = f.read()
nails = list(map(int,notes.split("\n")))
minimum = min(nails)
total = sum([n-minimum for n in nails])
print(f"Part  II: {total}")

with open(f"input3.txt", "r") as f: notes = f.read()
nails = sorted(list(map(int,notes.split("\n"))))
total, white, black = 0, 1, 1

while len(nails)>2:
  total += (nails[1]-nails[0])*white
  total += (nails[-1]-nails[-2])*black
  white += 1
  black += 1
  nails = nails[1:-1]

total += (nails[1] - nails[0]) * min(black, white)
print(f"Part III: {total}")
