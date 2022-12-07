with open("./input.txt", "r") as file:
    elves = []
    current_elf = 0
    for line in file:
        line = line.strip()
        if line == "":
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    elves.sort()
    print(elves[-1] + elves[-2] + elves[-3])
