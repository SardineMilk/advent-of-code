
total = 0
with open("day2.txt", "r") as file:
    line = file.read()
    data = line.split(",")

    for entry in data:

        a, b = entry.split("-")
        
        for i in range(int(a), int(b)+1):
            size = len(str(i))
                            

            for j in range(2, size+1):
                if (size%j)!=0:
                    continue

                chunk = size//j
                chunks = []
                for k in range(j):
                    start = chunk * k
                    end = chunk * (k+1)
                    
                    chunks.append(str(i)[start:end])
                
                chunkset = set(chunks)
                if len(chunkset) == 1:

                    #print(f"{i}, {chunk}")
                    total += i
                    break
    print(total)
