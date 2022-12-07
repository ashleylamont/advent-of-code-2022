with open('input') as file:
    overlaps = 0
    for line in file:
        line = line.strip()
        [elf1, elf2] = line.split(',')
        [elf1_lower, elf1_upper] = elf1.split('-')
        [elf2_lower, elf2_upper] = elf2.split('-')
        elf1_lower_overlap = int(elf2_lower) <= int(elf1_lower) <= int(elf2_upper)
        elf2_lower_overlap = int(elf1_lower) <= int(elf2_lower) <= int(elf1_upper)
        elf1_upper_overlap = int(elf2_lower) <= int(elf1_upper) <= int(elf2_upper)
        elf2_upper_overlap = int(elf1_lower) <= int(elf2_upper) <= int(elf1_upper)
        if elf1_lower_overlap or elf1_upper_overlap or elf2_lower_overlap or elf2_upper_overlap:
            overlaps += 1
    print(overlaps)