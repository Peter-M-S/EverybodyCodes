import math


def get_turns_and_wheels(notes):
  notes = notes.split("\n")
  turns = list(map(int, notes[0].split(",")))
  wheels = [[f] for f in notes[2].split()]
  for line in notes[3:]:
    i = 0
    while (i * 4 + 3) <= len(line):
      face = line[i * 4:i * 4 + 3]
      if face != "   ": wheels[i].append(face)
      i += 1
  return turns, wheels


def arrange(turns, wheels):
  result = wheels[:]
  for w, t in enumerate(turns):
    if t == 1: continue
    wheel = result[w]
    new_wheel = [wheel[0]]
    i = 0
    while len(wheel) - len(new_wheel):
      i += t
      new_wheel.append(wheel[i % len(wheel)])
    result[w] = new_wheel
  return result


def screen(n, wheels):
  faces = [n % len(w) for w in wheels]
  return " ".join([w[f] for w, f in zip(wheels, faces)])


def coins(counting):
  coins = 0
  for s in set(counting):
    s_n = counting.count(s)
    if s_n >= 3:
      coins += 1 + (s_n-3)
  return coins


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
turns, wheels = get_turns_and_wheels(notes)
wheels = arrange(turns, wheels)
part1 = screen(100, wheels)
print(f"Part   I: {part1}")


part2 = 0
N = 202420242024
with open(f"input2.txt", "r") as f: notes = f.read()
turns, wheels = get_turns_and_wheels(notes)
wheels = arrange(turns, wheels)

# I had the right idea to use lcm, but didi not figure it out correctly by myself. THX reddit!
repeater = math.lcm(*[len(w) for w in wheels])  # only length of wheels is relevant?
cycles, remainder = divmod(N, repeater)
total = final = 0
for n in range(1, repeater+1):
  counting = screen(n, wheels)[::2]
  total += coins(counting)
  if n == remainder: final = total
part2 = total * cycles + final
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
turns, wheels = get_turns_and_wheels(notes)
wheels_arranged = arrange(turns, wheels)
print(wheels, wheels_arranged)

# missing out Part 3

print(f"Part III: {part3}")
