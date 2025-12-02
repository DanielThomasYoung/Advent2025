with open('input.txt', 'r') as f:
    line = f.readline()

total = 0

id_ranges = line.split(',')

for id_range in id_ranges:
    split_range = id_range.split('-')
    start = int(split_range[0])
    end = int(split_range[1])

    for id in range(start, end + 1):
        id_len = len(str(id))
        
        if id_len % 2:
            continue

        first_half = str(id)[:id_len // 2]
        second_half = str(id)[id_len // 2:]
        if first_half == second_half:
            total += id

print(total)
