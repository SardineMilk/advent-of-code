with open("day6.txt", "r") as f:
    data = f.readlines()
    data = [line.split() for line in data]

total = 0

equation_num = len(data[0])
for i in range(equation_num):
    
    # Get equation
    equation = []
    for row in data[:-1]:
        equation.append(int(row[i]))

    if data[-1][i] == "+":
        total += sum(equation)
    else:
        product = 1
        for number in equation:
            product *= number
        total += product
print(total)