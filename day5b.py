with open("day5.txt", "r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

id_ranges = data[:data.index('')]
id_ranges = [id_range.split('-') for id_range in id_ranges]
id_ranges = [[int(first), int(second)] for first, second in id_ranges]


# Sort by starting point
id_ranges.sort(key=lambda x: x[0])

merged_ranges = []
current_start, current_end = id_ranges[0]

for start, end in id_ranges[1:]:
    # Next range overlaps current range?
    if start <= current_end + 1:
        # Merge them
        current_end = max(current_end, end)
    else:
        # No overlap 
        # Add previous range and start a new one
        merged_ranges.append([current_start, current_end])
        current_start, current_end = start, end

# Append the final interval
merged_ranges.append([current_start, current_end])

# Sum up all ranges
total = sum(end - (start - 1) for start, end in merged_ranges)
print(total)



