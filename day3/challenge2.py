with open('input', 'r') as file:
    total_priority = 0
    group_member = 0
    group_sacks = [None, None]
    for line in file:
        rucksack = line.strip()
        rucksack_chars = set()
        for char in rucksack:
            rucksack_chars.add(char)
        if group_member == 0:
            group_sacks[0] = rucksack_chars
            group_member = 1
        elif group_member == 1:
            group_sacks[1] = rucksack_chars
            group_member = 2
        else:
            group_sack_intersection = group_sacks[0].intersection(group_sacks[1], rucksack_chars)
            char = next(iter(group_sack_intersection))
            group_member = 0
            if char == char.upper():
                total_priority += ord(char) - ord('A') + 27
            else:
                total_priority += ord(char) - ord('a') + 1
    print(total_priority)