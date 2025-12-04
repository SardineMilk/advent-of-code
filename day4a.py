with open("day4.txt", "r") as f:
    data = f.readlines()

for i, line in enumerate(data):
    line = line.strip()
    data[i] = list(line)

total = 0
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value == ".": 
            continue

        adj = 0

        top = False
        bottom = False
        left = False
        right = False

        if (i==0):
            top = True
        if (i==len(data)-1):
            bottom = True

        if (j==0):
            left = True
        if (j==len(line)-1):
            right = True

        if not right:
            if data[i][j+1] == "@": adj+=1
        if not left:
            if data[i][j-1] == "@": adj+=1
        if not bottom:
            if not right:
                if data[i+1][j+1] == "@": adj+=1
            if data[i+1][j] == "@": adj+=1
            if not left:    
                if data[i+1][j-1] == "@": adj+=1
        if not top:
            if not right:
                if data[i-1][j+1] == "@": adj+=1
            if data[i-1][j] == "@": adj+=1
            if not left:    
                if data[i-1][j-1] == "@": adj+=1
        
        if adj < 4:
            total += 1


print(total)