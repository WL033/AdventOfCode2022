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


def scenicScore(row, column):
    currentNum = int(trees[row][column])
    product = 1

    # up
    counter = 0
    for r in reversed(range(0, row)):
        if int(trees[r][column]) < currentNum:
            counter += 1
        elif int(trees[r][column]) >= currentNum:
            counter += 1
            break

    product *= counter

    # down
    counter = 0
    for r in range(row + 1, numRow):
        if int(trees[r][column]) < currentNum:
            counter += 1
        elif int(trees[r][column]) >= currentNum:
            counter += 1
            break
    product *= counter

    # left
    counter = 0
    for c in reversed(range(0, column)):
        if int(trees[row][c]) < currentNum:
            counter += 1
        elif int(trees[row][c]) >= currentNum:
            counter += 1
            break
    product *= counter

    # right
    counter = 0
    for c in range(column + 1, numCol):
        if int(trees[row][c]) < currentNum:
            counter += 1
        elif int(trees[row][c]) >= currentNum:
            counter += 1
            break
    product *= counter

    return product


scenicScoreMatrix = []

for r in range(0, numRow):
    currentRow = []
    for c in range(0, numCol):
        if r == 0 or r == numRow - 1 or c == 0 or c == numCol - 1:
            currentRow.append(0)
        else:
            currentRow.append(scenicScore(r, c))

    scenicScoreMatrix.append(currentRow)

max = 0
for r in scenicScoreMatrix:
    for c in r:
        if c > max:
            max = c
print(max)


