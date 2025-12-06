with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
locations = set()

for (line_index, line) in enumerate(lines):
    for (char_index, char) in enumerate(line):
        if char == '@':
            locations.add((line_index, char_index))

for (paper_x, paper_y) in locations:
    adjacent = 0

    if (paper_x - 1, paper_y - 1) in  locations:
        adjacent += 1
    if (paper_x - 1, paper_y) in  locations:
        adjacent += 1
    if (paper_x - 1, paper_y + 1) in  locations:
        adjacent += 1
    if (paper_x, paper_y - 1) in  locations:
        adjacent += 1
    if (paper_x, paper_y + 1) in  locations:
        adjacent += 1
    if (paper_x + 1, paper_y - 1) in  locations:
        adjacent += 1
    if (paper_x + 1, paper_y) in  locations:
        adjacent += 1
    if (paper_x + 1, paper_y + 1) in  locations:
        adjacent += 1

    if adjacent < 4:
        total += 1


print(total)