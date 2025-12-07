from functools import lru_cache


@lru_cache(None)
def split(i, j):
    # Out of bounds horizontally
    if j < 0 or j >= len(data[i]):
        return 0

    # Bottom row = 1 completed timeline
    if i == len(data) - 1:
        return 1

    line = data[i]
    # Split
    if (line[j] == "^"):
        timelines = 0
        timelines += split(i+1, j-1) if j-1 >= 0 else 0
        timelines += split(i+1, j+1) if j+1 < len(line) else 0
        return timelines

    # Go straight down
    return split(i+1, j)  


with open("day7.txt") as f:
    data = tuple(f.readlines())


timelines = split(1, data[0].index("S"))
print(timelines)
    
