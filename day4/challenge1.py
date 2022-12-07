with open('input') as file:
    overlaps = 0
    for line in file:
        line = line.strip()
        [elf1, elf2] = line.split(',')
        [elf1_lower, elf1_upper] = elf1.split('-')
        [elf2_lower, elf2_upper] = elf2.split('-')
        if int(elf1_lower) >= int(elf2_lower) and int(elf1_upper) <= int(elf2_upper):
            overlaps += 1
        elif int(elf2_lower) >= int(elf1_lower) and int(elf2_upper) <= int(elf1_upper):
            overlaps += 1
    print(overlaps)