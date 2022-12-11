import numpy as np

with open("input.txt") as f:
    blob = f.read().split("\n")
    maxColumns = max(len(x) for x in blob)
    maxRows = len(blob)
    treeMap = np.zeros((maxRows, maxColumns))
    
    # Convert Map to Numpy Array
    row_index = 0
    for row in blob:
        col_index = 0
        for tree in row:
            treeMap[row_index][col_index] = tree
            col_index += 1
        row_index += 1
    print(treeMap)

    # Calculate Trees' Scenic Score
    treeScoreMap = np.zeros((maxRows, maxColumns))

    i = 1
    j = 2
    for row_index in range(1, maxRows - 1):#[i:i+1]:
        for col_index in range(1, maxColumns - 1):#[j:j+1]:
            row = treeMap[row_index]
            #print("Column: {}".format(row))
            column = treeMap[:,col_index]
            #print("Row: {}".format(column))
            treesLeft = 0
            treesRight = 0
            treesTop = 0
            treesBottom = 0
            #print("Tree: {}".format(treeMap[row_index][col_index]))
            for tree in column[row_index-1::-1]:
                treesTop += 1
                if tree >= treeMap[row_index][col_index]:
                    break
            #print("Top: {:} - {}".format(row[row_index-1::-1], treesTop))
            for tree in row[col_index-1::-1]:
                treesLeft += 1
                if tree >= treeMap[row_index][col_index]:
                    break
            #print("Left: {:} - {}".format(row[col_index-1::-1], treesLeft))
            for tree in row[col_index+1:]:
                treesRight += 1
                if tree >= treeMap[row_index][col_index]:
                    break
            #print("Right: {:} - {}".format(row[col_index+1:], treesRight))
            for tree in column[row_index+1:]:
                treesBottom += 1
                if tree >= treeMap[row_index][col_index]:
                    break
            #print("Bottom: {:} - {}".format(row[row_index+1:], treesBottom))
            treeScoreMap[row_index][col_index] = treesLeft * treesRight * treesTop * treesBottom

    print(treeScoreMap)
    print("Best Score: {:d}".format(int(treeScoreMap.max())))
    