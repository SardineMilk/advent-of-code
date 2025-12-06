import re

equations = []
with open("day6.txt", "r") as f:
    raw_lines = [line.rstrip("\n") for line in f]
    rows = [line.split() for line in raw_lines]

    # Determine number of columns
    num_cols = max(len(row) for row in rows)

    # Find max width of each column
    col_widths = [0] * num_cols
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    starts = []
    pos = 0

    for w in col_widths:
        starts.append((pos, pos + w))
        pos += w + 1   # +1 for the single-space separator

    columns = [[] for _ in col_widths]

    for line in raw_lines:
        for i, (s, e) in enumerate(starts):
            cell = line[s:e]
            columns[i].append(cell)


total = 0

for i, col in enumerate(columns, start=1):
    equation = col[:-1]

    octo_equation = ["" for _ in range(len(col[0]))]
    for number in equation:
        for i, digit in enumerate(number):
            if digit == " ":
                continue
            octo_equation[i] += digit

    octo_equation = list(map(int, octo_equation))
    if col[-1].strip() == "+":
        total += sum(octo_equation)
    else:
        product = 1
        for number in octo_equation:
            product *= number
        total += product
        
print(total)