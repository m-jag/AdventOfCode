#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read().split("\n")
    sum = 0

    for rucksack_a, rucksack_b, rucksack_c in zip(blob[::3], blob[1::3], blob[2::3]):
        overlap = list(set(rucksack_a).intersection(list(set(rucksack_b).intersection(rucksack_c))))
        #print("overlap: {overlap:}".format(overlap = overlap))

        if len(overlap) > 1:
            print("Too many overlapping")
        elif len(overlap) < 0:
            print("Too few overlapping")
        else:
            item = ord(overlap[0])
            prio = 0
            if item >= ord('a') and item <= ord('z'):
                prio = item - ord('a') + 1
            elif item >= ord('A') and item <= ord('Z'):
                prio = item - ord('A') + 27
            else:
                print("Unexpected char {item:c}".format(item = item))
            #print("prio: {prio:d}".format(prio = prio))
            sum += prio
    print("sum: {sum:d}".format(sum = sum))