part = 1
with open(f"input1.txt", "r") as f: notes = f.read()
blocks = int(notes.strip())
layer, width = 0, 1
struct = [1 * width]
blocks -= 1
while blocks:
  if struct[layer] == width:
    layer += 1
    struct.append(1)
    blocks -= 1
    width += 2
  else:
    missing_blocks = width - struct[layer]
    delta = min(missing_blocks, blocks)
    struct[layer] += delta
    blocks -= delta

missing_blocks = width - struct[layer]
print(f"Part   I: {missing_blocks * width}")


part = 2
with open(f"input2.txt", "r") as f: notes = f.read()
f = int(notes.strip())
blocks, aco = 20240000, 1111
layer, thick, width = 0, 1, 1
struct = [1 * width * thick]
blocks -= thick * width
while blocks:
  if struct[layer] == thick * width:
    layer += 1
    struct.append(1)
    blocks -= 1
    thick = (thick * f) % aco
    width += 2
  else:
    missing_blocks = width * thick - struct[layer]
    delta = min(missing_blocks, blocks)
    struct[layer] += delta
    blocks -= delta

missing_blocks = width * thick - struct[layer]
print(f"Part  II: {missing_blocks * width}")


part = 3


def get_cols(struct) -> list:
  cols = []
  for layer, n in enumerate(struct):
    width = layer*2 + 1
    thick = int(n / width)
    cols = [thick] if width == 1 else [thick] + [h+thick for h in cols] + [thick]
  return cols


def get_removes(cols) -> int:
  removes = 0
  width = len(cols)
  for n in cols[1:-1]:
    removes += (f * width * n) % aco
  return removes


with open(f"input3.txt", "r") as f: notes = f.read()
f = int(notes.strip())  # 2
blocks, aco = 202400000, 10  # 160, 5
layer, thick, width = 0, 1, 1
struct = [1 * width * thick]
blocks -= thick * width
while blocks:
  if struct[layer] == thick * width:
    layer += 1
    struct.append(1)
    blocks -= 1
    thick = (thick * f) % aco + aco
    width += 2
  else:
    missing_blocks = width * thick - struct[layer]
    delta = min(missing_blocks, blocks)
    struct[layer] += delta
    blocks -= delta

missing_blocks = width * thick - struct[layer]

# fill theoretical last layer
struct[-1] += missing_blocks

# remove blocks
removes = get_removes(get_cols(struct))
if missing_blocks < removes: print("could start a new layer...")
print(f"Part III: {missing_blocks-removes}")
