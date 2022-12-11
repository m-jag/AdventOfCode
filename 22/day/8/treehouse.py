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

    # Calculate Visible Trees
    visibleTreeMap = np.ones((maxRows, maxColumns))

    for row_index in range(1, maxRows - 1):
        for col_index in range(1, maxColumns - 1):
            row = treeMap[row_index]
            #print("Column: {}".format(row))
            column = treeMap[:,col_index]
            #print("Row: {}".format(column))
            visibleLeft = True
            visibleRight = True
            visibleTop = True
            visibleBottom = True
            #print("Tree: {}".format(treeMap[row_index][col_index]))
            for tree in row[:col_index]:
                visibleLeft = visibleLeft and tree < treeMap[row_index][col_index]
            #print("Left: {:} - {}".format(row[:col_index], visibleLeft))
            for tree in row[col_index+1:]:
                visibleRight = visibleRight and tree < treeMap[row_index][col_index]
            #print("Right: {:} - {}".format(row[col_index+1:], visibleRight))
            for tree in column[:row_index]:
                visibleTop = visibleTop and tree < treeMap[row_index][col_index]
            #print("Top: {:} - {}".format(row[:row_index], visibleTop))
            for tree in column[row_index+1:]:
                visibleBottom = visibleBottom and tree < treeMap[row_index][col_index]
            #print("Bottom: {:} - {}".format(row[row_index+1:], visibleBottom))
            visibleTreeMap[row_index][col_index] = visibleLeft or visibleRight or visibleTop or visibleBottom

    print(visibleTreeMap)
    print("Number of Visible Trees {:}".format(int(np.sum(visibleTreeMap))))
    