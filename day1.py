

current_position = 50
zero_count = 0
with open("day1.txt", "r") as file:
    for line in file:
        direction = line[0]
        step_count = int(line[1:])

        if direction == "L":
            step_direction = -1
        elif direction == "R":
            step_direction = 1

        for _ in range(step_count):
            current_position = (current_position + step_direction) % 100

            if current_position == 0:
                zero_count += 1
                
    print("zero_count")    
    
        