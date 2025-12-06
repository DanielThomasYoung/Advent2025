with open('input.txt', 'r') as f:
    raw_lines = f.readlines()
    lines = []
    for line in raw_lines:
        lines.append(line.strip())

total = 0
id_ranges = set()
unprocessed_id_ranges = set()

for line in lines:
    if not line:
        break

    start_and_end = line.split('-')
    start = int(start_and_end[0])
    end = int(start_and_end[1])
    unprocessed_id_ranges.add((start, end))


while unprocessed_id_ranges:
    processing_range = unprocessed_id_ranges.pop()
    start = processing_range[0]
    end = processing_range[1]
    add_ids = True

    for id_range in id_ranges:
        # subset
        if start >= id_range[0] and end <= id_range[1]:
            add_ids = False
            continue

        # left overlap
        if start < id_range[0] and end <= id_range[1] and end >= id_range[0]:
            end = id_range[0] - 1

        # right overlap
        if start >= id_range[0] and start <= id_range[1] and end > id_range[1]:
            start = id_range[1] + 1

        # superset
        if start < id_range[0] and end > id_range[1]:
            unprocessed_id_ranges.add((id_range[1] + 1, end))
            end = id_range[0] - 1

    if add_ids:
        id_ranges.add((start, end))
        total += end - start + 1

print(f"total {total}")
