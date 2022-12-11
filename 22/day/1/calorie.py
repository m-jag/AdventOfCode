#!/usr/bin/env python3
with open("input.txt") as f:
    blob = f.read()
    elves = blob.split("\n\n")
    max_cal_elf_num = -1
    max_cal = 0
    elf_num = 0

    for elf in elves:
        sum_cal = 0
        for val in elf.split():
            sum_cal += int(val)
        if (sum_cal > max_cal):
            max_cal_elf_num = elf_num
            max_cal = sum_cal
        elf_num += 1
    
    print("Max Calories: {max_cal_elf_num:d}".format(max_cal_elf_num = max_cal_elf_num))
    print("Max Calories: {max_cal:d}".format(max_cal = max_cal))