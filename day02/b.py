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

        for i in range(1, id_len//2 + 1):
            invalid_id = True
            
            if id_len % i:
                continue

            compare_str = ""
            start_slice = 0
            end_slice = i

            while end_slice <= id_len:
                current_slice = str(id)[start_slice:end_slice]

                if compare_str and current_slice != compare_str:
                    invalid_id = False
                    break
                else:
                    compare_str = current_slice
                    start_slice += i
                    end_slice += i

            if invalid_id:
                total += id
                break

print(total)
