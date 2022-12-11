# Unique Sequence Detector (len = 4)

with open("input.txt") as f:
    stream = f.read()
    sequence = []
    num_chars = 0
    for char in stream:
        num_chars += 1
        while (len(sequence) >= 4):
            sequence.pop(0)
        sequence.append(char)
        if (len(sequence) == 4):
            unique_list = []
            for x in sequence:
                if x not in unique_list:
                    unique_list.append(x)
            if len(unique_list) == len(sequence):
                break
print("Num Chars Processed: {num_chars:d}".format(num_chars = num_chars))