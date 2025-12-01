with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
dial = 50
for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == 'R':
        dial += amount
    else:
        dial -= amount

    dial = dial % 100
    
    if dial == 0:
        total += 1

print(total)
