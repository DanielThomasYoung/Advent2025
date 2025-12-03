with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = ""

    remaining_digits = 12

    while remaining_digits:
        # print(line[:-remaining_digits])
        next_digit = max(line[:-remaining_digits])
        digits += next_digit

        max_index = line.index(next_digit) + 1
        line = line[max_index:]

        remaining_digits -= 1

    total += int(digits)

print(total)