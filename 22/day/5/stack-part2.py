#!/usr/bin/env python3
import re
STACK_WIDTH=9

def printStack(stacks):
    tallestStack = max(len(x) for x in stacks)
    for heightPos in range(tallestStack)[::-1]:
        for stackNum in range(STACK_WIDTH):
            if len(stacks[stackNum]) > heightPos:
                print("[{:s}]".format(stacks[stackNum][heightPos]), end="")
            else:
                print("   ", end="")
            if (stackNum < STACK_WIDTH - 1):
                print(" ", end="")
            else:
                print("")
    for i in range(STACK_WIDTH):
        print(" {:d}  ".format(i + 1), end="")
    print("")

with open("input.txt") as f:
    blob = f.read().split("move")

    stack=blob[0].split("\n")[:-3]
    # Parse Diagram
    stacks = []
    for i in range(STACK_WIDTH):
        stacks.append([])

    for line in stack[-1::-1]:
        for index in range(STACK_WIDTH):
            item = line[index * 4 + 1]
            if (item != ' '):
                stacks[index].append(item)
    print("Stack:")
    printStack(stacks)

    # Process Moves
    moves=blob[1:]
    print("Moves: {moves:d}".format(moves=len(moves)))
    moveRegex = re.compile(r"(?P<amt>\d+?) from (?P<src>\d+?) to (?P<dst>\d+?)")
    for move in moves:
        move = move.strip()
        #print("move {move:s}".format(move = move))
        match = moveRegex.match(move)
        amt = match.group("amt")
        src = match.group("src")
        dst = match.group("dst")
        #print("move {amt:s} from {src:s} to {dst:s}".format(amt=amt, src=src, dst = dst))
        moving_stack = []
        for _ in range(int(amt)):
            moving_stack.append(stacks[int(src) - 1].pop())
        for crate in moving_stack[::-1]:
            stacks[int(dst) - 1].append(crate)
        #printStack(stacks)
    printStack(stacks)