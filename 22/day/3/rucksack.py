#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read().split("\n")
    sum = 0

    for rucksack in blob:
        split_point = int(len(rucksack)/2)
        first_comp = rucksack[:split_point]
        second_comp = rucksack[split_point:]
        
        #print("first_comp: {first_comp:s}".format(first_comp = first_comp))
        #print("second_comp: {second_comp:s}".format(second_comp = second_comp))

        overlap = list(set(first_comp).intersection(second_comp))
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
            
    