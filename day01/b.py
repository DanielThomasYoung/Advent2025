with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
dial = 50
for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == 'R':
        dial += amount
        total += dial//100
    else:
        dial = (100 - dial) % 100
        dial += amount
        total += dial//100

        dial = (100 - dial)

    dial = dial % 100
    

print(total)
