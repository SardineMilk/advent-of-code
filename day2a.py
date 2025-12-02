
total = 0
with open("day2.txt", "r") as file:
    line = file.read()
    data = line.split(",")

    for entry in data:
        a, b = entry.split("-")
        
        for i in range(int(a), int(b)):
            size = len(str(i))
            mid = size//2
            if str(i)[0:mid] == str(i)[mid:size]:
                total += i
    
    print(total)
