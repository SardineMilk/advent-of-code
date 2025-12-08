import math
from collections import defaultdict

processed_data = []
with open("day8.txt") as f:
    data = f.readlines()
    for line in data:
        x, y, z = [int(x) for x in line.split(',')]
        processed_data.append((x, y, z))

def getDist(a, b):
    ax, ay, az = a
    bx, by, bz = b
    dist = math.sqrt((ax-bx)**2 + (ay-by)**2 + (az-bz)**2)

    return dist


# Get the distance for every a, b combination (a!=b)
# Sort by distance ascending
# Add the indices to a list of lists
# If any new combinations contain an index in a list, add to that list
# Otherwise make a new list

combinations = []
for i in range(len(processed_data)):
    for j in range(len(processed_data)):
        dist = getDist(processed_data[i], processed_data[j])

        if (i>j): 
            combinations.append((dist, i, j))

combinations.sort(key=lambda x: x[0])

data_dict = {i: i for i in range(len(processed_data))}
def find(x):
    if x==data_dict[x]:
        return x
    data_dict[x] = find(data_dict[x])
    return data_dict[x]

def mix(x, y):
    data_dict[find(x)] = find(y)

for _dist, i, j in combinations[:1000]:
    
    mix(i, j)


circuits = defaultdict(int)
for x in range(len(processed_data)):
    circuits[find(x)] += 1
final = sorted(circuits.values())

    
print(final[-1]*final[-2]*final[-3])