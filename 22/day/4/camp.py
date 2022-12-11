#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read().split("\n")
    
    count = 0

    for line in blob:
        pair1 = line.split(",")[0].split('-')
        pair2 = line.split(",")[1].split('-')
        #print("-------------")
        #print("pair1: {pair1:}".format(pair1=pair1))
        #print("pair2: {pair2:}".format(pair2=pair2))
        #print("-------------")

        a = int(pair1[0]) - int(pair2[0])
        b = int(pair1[1]) - int(pair2[1])
        if a == 0 or b == 0 or a / abs(a) != b / abs(b):
            count += 1
        #print("Count: {count:d}".format(count=count))

    print("Count: {count:d}".format(count=count))