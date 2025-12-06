with open('input.txt', 'r') as f:
    raw_lines = f.readlines()
    lines = []
    for line in raw_lines:
        lines.append(line.strip())

total = 0
building_ranges = True
fresh_ids = set()

for line in lines:
    if not line:
        building_ranges = False
        continue

    if building_ranges:
        start_and_end = line.split('-')

        fresh_ids.add((int(start_and_end[0]), int(start_and_end[1])))
        
    else:
        id = int(line)

        for id_range in fresh_ids:
            if id >= id_range[0] and id <= id_range[1]:
                total += 1
                break

print(total)