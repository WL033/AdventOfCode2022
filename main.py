with open('input.txt', 'r') as f:
    lines = f.readlines()
    trees = [entry.strip() for entry in lines]

numRow = len(trees)
numCol = len(trees[0])

# Create a function that will parse up, down, left, right to see if all those numbers are less than the target number
# Parse through each tree:
# if it is an edge tree, it is automatically visible
# if it is a non-edge tree, pass the current row and column index through the function.
# Create a boolean matrix for to record which trees are visible
def allTrue(list):
    for element in list:
        if not element:
            return False
    return True


def isVisible(row, column):
    currentNum = int(trees[row][column])
    # up
    uBoolList = []
    for r in range(0, row):
        if int(trees[r][column]) < currentNum:
            uBoolList.append(True)
        else:
            uBoolList.append(False)
    if allTrue(uBoolList):
        return True

    # down
    dBoolList = []
    for r in range(row + 1, numRow):
        if int(trees[r][column]) < currentNum:
            dBoolList.append(True)
        else:
            dBoolList.append(False)
    if allTrue(dBoolList):
        return True

    # left
    lBoolList = []
    for c in range(0, column):
        if int(trees[row][c]) < currentNum:
            lBoolList.append(True)
        else:
            lBoolList.append(False)
    if allTrue(lBoolList):
        return True

    # right
    rBoolList = []
    for c in range(column + 1, numCol):
        if int(trees[row][c]) < currentNum:
            rBoolList.append(True)
        else:
            rBoolList.append(False)
    if allTrue(rBoolList):
        return True

    return False


truthMatrix = []

for r in range(0, numRow):
    currentRow = []
    for c in range(0, numCol):
        if r == 0 or r == numRow-1 or c == 0 or c == numCol-1:
            currentRow.append(True)
        else:
            currentRow.append(isVisible(r, c))

    truthMatrix.append(currentRow)

count = 0
for r in truthMatrix:
    for c in r:
        if c:
            count += 1

print(count)