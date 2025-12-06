with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
locations = set()
to_remove = set()
looping = True

for (line_index, line) in enumerate(lines):
    for (char_index, char) in enumerate(line):
        if char == '@':
            locations.add((line_index, char_index))

while looping:
    looping = False
    to_remove.clear()


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
            to_remove.add((paper_x, paper_y))
            total += 1
            looping = True

    locations -= to_remove


print(total)