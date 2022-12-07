with open("./input.txt", "r") as file:
    highest_calories = 0
    current_calories = 0
    for line in file:
        line = line.strip()
        if line == "":
            highest_calories = max(current_calories, highest_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    print(highest_calories)
