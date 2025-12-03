with open("day3.txt", "r") as file:
    data = file.readlines()

    total = 0

    for line in data:
        line.strip()

        highest = -1
        for i in range(len(line)):
            for j in range(len(line)):
                if i>=j: continue

                current = int(line[i] + line[j])

                highest = max(highest, current)
        total += highest


    print(total)