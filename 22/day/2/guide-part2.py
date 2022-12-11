#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read().split("\n")
    score = 0

    for line in blob:
        selection = line.split(" ")
        opponent = ord(selection[0]) - ord('A') + 1
        result = ord(selection[1]) - ord('X') + 1

        if (result == 1): # Lose
            print("Lose")
            you = opponent - 1
            if you == 0: you = 3
        elif (result == 2): # Tie
            print("Tie")
            you = opponent
            score += 3
        else: # Win
            print("Win")
            you = opponent % 3 + 1
            score += 6
        
        print("You: {you:d}".format(you = you))
        print("Opponent: {opponent:d}".format(opponent = opponent))
        score += you
        
        
    print("Score: {score:d}".format(score = score))