WORDS = ["LOR","LL","SI","OR","OL","DO","CO"]
TEXT = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM."

total = sum(TEXT.count(w) for w in WORDS)
print(f"Part   I: {total}")

with open("input2.txt", "r") as f: notes = f.read()
WORDS, TEXT = notes.split("\n\n")
WORDS = set(WORDS[6:].split(","))
WORDS |= set([str(w[::-1]) for w in WORDS])
lines = TEXT.split("\n")

coord_record = set()
for w in WORDS:
  wl = len(w)
  i = 0
  for line in lines:
    for j in range(len(line)-wl+1):
      t = line[j:j+wl]
      if t == w:
        coord_record |= set([i+k for k in range(j,j+wl)])
    i += len(line)
print(f"Part  II: {len(coord_record)}")

coord_record = set()

with open("input3.txt", "r") as f: notes = f.read()
WORDS, TEXT = notes.split("\n\n")
WORDS = set(WORDS[6:].split(","))
WORDS |= set([str(w[::-1]) for w in WORDS])
lines = TEXT.split("\n")
columns = ["".join(s) for s in zip(*lines)]
# print(lines)
# print(columns)

for w in WORDS:
  wl = len(w)
  for row, line in enumerate(lines):
    for col in range(len(line)):
      test_line = line[col:]+line[:col]  # lines do loop
      if test_line[:wl] == w:
        coord_record |= set([(row, c % len(line)) for c in range(col, col + wl)])

  for col, column in enumerate(columns):
    for row in range(len(column)-wl+1):
      test_word = column[row:row+wl]              # rows do not loop
      if test_word == w:
        coord_record |= set([(r, col) for r in range(row, row + wl)])
print(f"Part III: {len(coord_record)}")

