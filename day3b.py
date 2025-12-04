with open("day3.txt", "r") as file:
    data = file.readlines()

    total = 0

    for line in data:
        line = line.strip()
        line = list(map(int, line))

        highest = ""

        start_index = 0  
        end_index = 0  

        need = 12

        for i in range(12):
            # Exclude the required digits from the end of the list
            end_index = len(line) - (need-1)  

            # Find the max index in the given slice
            max_index = max(range(start_index, end_index), key=lambda i: line[i])  

            highest += str(line[max_index])

            start_index = max_index+1
            need -= 1

        total += int(highest)

    print(total)