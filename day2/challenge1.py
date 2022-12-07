with open('input', 'r') as file:
    score = 0
    winning_matches = {
        "A": "Z",
        "B": "X",
        "C": "Y",
        "Z": "B",
        "Y": "A",
        "X": "C"
    }
    choice_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    for line in file:
        line = line.strip()
        [opponent, player] = line.split(' ')
        match_score = 0
        match_score += choice_points[player]
        if winning_matches[opponent] == player:
            # Loss - 0 points
            pass
        elif winning_matches[player] == opponent:
            # Win - 6 points
            match_score += 6
        else:
            # Draw - 3 points
            match_score += 3
        score += match_score
    print(score)
