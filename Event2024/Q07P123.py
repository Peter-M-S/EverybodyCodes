import itertools
import math


def get_total(actions: list|tuple, sections: str, level: int = 10) -> int:
  total = 0
  for j, s in enumerate(sections):
    i = j % len(actions)
    a = actions[i]
    if s == "+":
      level += 1
    elif s == "-":
      level -= 1
    elif a == "+":
      level += 1
    elif a == "-":
      level -= 1
    level = max(level, 0)
    total += level
  return total


def get_track(track_notes: str) -> str:
  grid = track_notes.split("\n")
  pos = 0 + 1j   # real = row, imag = col
  direction = (0+1j)
  track: str = grid[int(pos.real)][int(pos.imag)]
  while track[-1] != "S":
    direction = -direction
    for _ in range(3):
      direction = 1j * direction
      n_pos = pos + direction
      if n_pos.real < 0 or n_pos.real >= len(grid): continue
      if n_pos.imag < 0 or n_pos.imag >= len(grid[int(n_pos.real)]): continue
      s = grid[int(n_pos.real)][int(n_pos.imag)]
      if s == " ": continue
      track += s
      pos = n_pos
      break
  return track


part = 1
with open(f"input1.txt", "r") as f: notes = f.read()
rankings = []
for line in notes.split("\n"):
  sections = "="*10
  plan, actions = line.split(":")
  actions = actions.split(",")
  total = get_total(actions, sections)
  rankings.append((total, plan))
part = "".join([p[1] for p in sorted(rankings, reverse=True)])
print(f"Part   I: {part}")


part = 2 
with open(f"input2.txt", "r") as f: notes = f.read()
plan_notes, track_notes = notes.split("\n\n")
laps = 10
plans = dict()
for line in plan_notes.split("\n"):
  plan, actions = line.split(":")
  plans[plan] = actions.split(",")

track = get_track(track_notes)
sections = track*laps

rankings = []
for plan, actions in plans.items():
  total = get_total(actions, sections)
  rankings.append((total, plan))
part = "".join([p[1] for p in sorted(rankings, reverse=True)])
print(f"Part  II: {part}")


part = 3
laps = 2024
with open(f"input3.txt", "r") as f: notes = f.read()
opp_actions, track_notes = notes.split("\n\n")
opp_actions = opp_actions[2:].split(",")

pool = "+"*5+"-"*3+"="*3

# track = get_track(track_notes)
track = "+=+++===-+++++=-==+--+=+===-++=====+--===++=-==+=++====-==-===+=+=--==++=+========-=======++--+++=-++=-+=+==-=++=--+=-====++--+=-==++======+=++=-+==+=-==++=-=-=---++=-=++==++===--==+===++===---+++==++=+=-=====+==++===--==-==+++==+++=++=+===--==++--===+=====-=++====-+=-+--=+++=-+-===++====+++--=++====+=-=+===+=====-+++=+==++++==----=+=+=-S"
lcm = math.lcm(len(pool), len(track))
min_laps = lcm / len(track)
assert min_laps == int(min_laps)
sections = track * int(min_laps)
# after this number the (actions, track)-sequence loops
# len(sections) = 340 track-fields * 11 rounds = 11 actions * 340 action-cycles
print(len(sections))

benchmark = get_total(opp_actions, sections)

wins: int = 0

all_actions = set(itertools.permutations(pool))
print(len(all_actions))
for actions in all_actions:
  wins += get_total(actions, sections) > benchmark

print(f"Part III: {wins}")
