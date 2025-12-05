with open("day5.txt", "r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

ranges, ids = data[:data.index('')], data[data.index('')+1:]

total_fresh = 0
for value in ids:
    value = int(value)

    fresh = False
    for id_range in ranges:
        first, second = id_range.split('-')
        first, second = int(first), int(second)

        if (value >= first) and (value <= second):
            fresh = True
            break

    if fresh:
        total_fresh += 1

print(total_fresh)
