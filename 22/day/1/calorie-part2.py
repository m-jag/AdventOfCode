#!/usr/bin/env python3
TOP_COUNT = 3
with open("input.txt") as f:
    blob = f.read()
    elves = blob.split("\n\n")
    cal_list = []

    for elf in elves:
        sum_cal = 0
        for val in elf.split():
            sum_cal += int(val)
        cal_list.append(sum_cal)
        if len(cal_list) > TOP_COUNT:
            cal_list.sort(reverse=True)
            cal_list.pop()
        print(cal_list)
    print("Calories Sum: {cal_sum:d}".format(cal_sum = sum(cal_list)))