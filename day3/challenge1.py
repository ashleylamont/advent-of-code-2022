with open('input', 'r') as file:
    total_priority = 0
    for line in file:
        rucksack = line.strip()
        compartment_a = rucksack[0:int(len(rucksack)/2)]
        compartment_b = rucksack[int(len(rucksack)/2):]
        comp_a_types = set()
        for char in compartment_a:
            comp_a_types.add(char)
        for char in compartment_b:
            if char in comp_a_types:
                if char == char.upper():
                    total_priority += ord(char)-ord('A')+27
                else:
                    total_priority += ord(char)-ord('a')+1
                break
    print(total_priority)