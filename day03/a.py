with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    first_digit = max(line[:-2])
    max_index = line.index(first_digit) + 1
    remaining = line[max_index:]
    second_digit = max(remaining)
    total += int(first_digit + second_digit)

print(total)