part = 1
stamps = [1, 3, 5, 10]
with open(f"input1.txt", "r") as f: notes = f.read()
total = 0
for n in map(int, notes.split("\n")):
  for s in stamps[::-1]:
    while n >= s:
      total += n // s
      n = n % s
print(f"Part   I: {total}")


part = 2
with open(f"input2.txt", "r") as f: notes = f.read()
notes = list(map(int, notes.split("\n")))
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
# this algo with explanation of AI for the coin-problem
max_n = max(notes)
min_beetles = [0] + [float("inf")] * max_n
for i in range(1, max_n+1):
  for s in stamps:
    if i >= s:
      summands = min_beetles[i - s] + 1
      min_beetles[i] = min(min_beetles[i], summands)
part = sum([min_beetles[i] for i in notes])
print(f"Part  II: {part}")


part = 3
with open(f"input3.txt", "r") as f: notes = f.read()
notes = list(map(int, notes.split("\n")))
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
max_d = 100
hi_of_pairs = [int(n / 2 + 0.5) + 50 for n in notes]  # get start values for iteration through max difference range
max_n = max(hi_of_pairs)

# this algo with explanation of AI for the coin-problem
min_beetles = [0] + [float("inf")] * max_n
for i in range(1, max_n+1):
  for s in stamps:
    if i >= s:
      summands = min_beetles[i - s] + 1
      min_beetles[i] = min(min_beetles[i], summands)

total = 0
for p_hi, n in zip(hi_of_pairs, notes):
  beetles = float("inf")
  p_lo = n - p_hi
  while p_lo <= p_hi:
    if p_hi-p_lo <= max_d:
      beetles = min(beetles, min_beetles[p_hi] + min_beetles[n - p_hi])
    p_hi -= 1
    p_lo = n-p_hi
  total += beetles
print(f"Part III: {total}")
