with open("day7.txt") as f:
    data = f.readlines()


total_splits = 0
beams = {data[0].index("S")}
for line in data[1:]:
    new_beams = []
    for i in range(len(line)):

        if (line[i] == ".") and (i in beams):
            new_beams.append(i)
        
        if (line[i] == "^") and (i in beams):
            total_splits += 1
            new_beams.append(i-1)
            new_beams.append(i+1)
    
    beams = set(new_beams)

print(total_splits)
    
