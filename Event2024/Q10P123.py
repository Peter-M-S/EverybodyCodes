
def get_symbols(grid) -> tuple[list, list]:
  rows, cols = [], []
  for row, col in zip(grid, zip(*grid)):
    if row[0] == "*": continue
    rows.append(set([s for s in row if s != "."]))
    cols.append(set([s for s in col if s != "."]))
  return rows, cols


def get_word(grid, rows=None, cols=None) -> str:
  if rows is None and cols is None:
    rows, cols = get_symbols(grid)
  word = ""
  for r in range(4):
    for c in range(4):
      s = rows[r] & cols[c]
      word += list(s)[0] if s else "."
  return word


def get_power(word) -> int:
  power = 0
  # if not word: return power
  for i, s in enumerate(word, start=1):
    power += i * (ord(s) - 64)
  return power


part1 = 0
with open(f"input1.txt", "r") as f: notes = f.read()
grid = notes.split("\n")
print(f"Part   I: {get_word(grid)}")


part2 = 0
with open(f"input2.txt", "r") as f: notes = f.read()
all_grids = []
notes = notes.split("\n\n")
for note in notes:
  grids = note.split("\n")[0].split()
  for line in note.split("\n")[1:]:
    for i, _ in enumerate(grids): grids[i] += "\n" + line.split()[i]
  all_grids += grids
part2 = sum(get_power(get_word(grid.split("\n"))) for grid in all_grids)
print(f"Part  II: {part2}")


part3 = 0
with open(f"input3.txt", "r") as f: notes = f.read()
wall = [[*line] for line in notes.split("\n")]  # 2D list of char
start_rows = list(range(0, len(wall) - 2, 6))
start_cols = list(range(0, len(wall[0]) - 2, 6))
grids_in_wall = []
for r in start_rows:
  for c in start_cols: grids_in_wall.append((r, c))
# print(grids_in_wall)
solved_grids, unsolved_grids = set(), set()
last_unsolved = len(grids_in_wall)
while len(unsolved_grids) != last_unsolved:
  last_unsolved = len(unsolved_grids)
  for r0, c0 in grids_in_wall:
    if (r0, c0) in solved_grids: continue
    grid = [[wall[r][c] for c in range(c0, c0 + 8)] for r in range(r0, r0 + 8)]
    solvable = True

    row_sym, col_sym = get_symbols(grid)
    word = get_word(grid, row_sym, col_sym)
    # paste word into grid
    for r in range(4):
      for c in range(4): grid[2 + r][2 + c] = word[r * 4 + c]

    dots = [i for i, s in enumerate(word) if s == "."]
    for rc in dots:
      r, c = rc // 4, rc % 4
      seen = {*word[r * 4:r * 4 + 4]} | {word[i * 4 + c] for i in range(4)}
      seen -= {"."}
      symbols = set(row_sym[r]) | set(col_sym[c])
      symbols -= {"?"}
      missing = list(symbols - seen)

      if len(missing) != 1:
        solvable = False
        unsolved_grids.add((r0, c0))
        continue

      # replace "." by missing[0]
      grid[2 + r][2 + c] = missing[0]

      # find "?" in grid row or column and replace it. "?" not necessary present
      if "?" in grid[2 + r]:
        i = grid[2 + r].index("?")
        grid[2 + r][i] = missing[0]
      elif "?" in [grid[r][2 + c] for r in range(8)]:
        i = [grid[r][2 + c] for r in range(8)].index("?")
        grid[i][2 + c] = missing[0]

      row_sym, col_sym = get_symbols(grid)
      word = get_word(grid, row_sym, col_sym)

    if solvable:
      value = get_power(word)
      solved_grids.add((r0, c0))
      # paste solved grid into wall
      for i, line in enumerate(grid): wall[r0 + i][c0:c0+len(line)] = line
      part3 += value

print(f"Part III: {part3}")
