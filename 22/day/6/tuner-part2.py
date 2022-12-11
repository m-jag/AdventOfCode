# Unique Sequence Detector (len = 14)
LEN = 14

with open("input.txt") as f:
    stream = f.read()
    sequence = []
    num_chars = 0
    for char in stream:
        num_chars += 1
        while (len(sequence) >= LEN):
            sequence.pop(0)
        sequence.append(char)
        if (len(sequence) == LEN):
            unique_list = []
            for x in sequence:
                if x not in unique_list:
                    unique_list.append(x)
            if len(unique_list) == len(sequence):
                break
print("Num Chars Processed: {num_chars:d}".format(num_chars = num_chars))