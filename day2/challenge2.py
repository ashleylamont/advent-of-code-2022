with open('input', 'r') as file:
    score = 0
    win = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }
    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    lose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }
    choice_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    names = {
        "A": "Rock      ",
        "B": "Paper     ",
        "C": "Scissors  ",
        "X": "Rock      ",
        "Y": "Paper     ",
        "Z": "Scissors  "
    }
    for line in file:
        line = line.strip()
        [opponent, player] = line.split(' ')
        match_score = 0
        if player == "X":
            # We need to lose
            player_choice = lose[opponent]
            match_score += choice_points[player_choice]
            print(f"<{line}> [O] {names[opponent]} beats     [P] {names[player_choice]} => {choice_points[player_choice]} + 0 = {match_score}")
        elif player == "Y":
            # We need to draw
            player_choice = draw[opponent]
            match_score += choice_points[player_choice] + 3
            print(f"<{line}> [O] {names[opponent]} draws     [P] {names[player_choice]} => {choice_points[player_choice]} + 3 = {match_score}")
        else:
            # We need to win
            player_choice = win[opponent]
            match_score += choice_points[player_choice] + 6
            print(f"<{line}> [O] {names[opponent]} loses to  [P] {names[player_choice]} => {choice_points[player_choice]} + 6 = {match_score}")
        score += match_score
    print(score)
