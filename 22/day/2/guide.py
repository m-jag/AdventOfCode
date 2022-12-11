#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read().split("\n")
    score = 0

    for line in blob:
        selection = line.split(" ")
        opponent = ord(selection[0]) - ord('A') + 1
        you = ord(selection[1]) - ord('X') + 1
        #print("You: {you:d}".format(you = you))
        #print("Opponent: {opponent:d}".format(opponent = opponent))
        score += you
        if (you == opponent): # Tie
            score += 3
        elif (you % 3 == (opponent + 1) % 3): # Win
            score += 6
                
    print("Score: {score:d}".format(score = score))