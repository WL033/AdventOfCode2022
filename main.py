with open('input.txt', 'r') as f:
    lines = f.readlines()
    trees = [entry.strip() for entry in lines]

numRow = len(trees)
numCol = len(trees[0])


def visible(target, sides):
    larger = False
    for num in sides:
        if target > num:
            larger = True
        else:
            larger = False
    return larger


visibilityChart = []
for r in range(0, numRow):
    row = []
    for c in range(0, numCol):
        if c == 0 or c == numCol - 1 or r == 0 or r == numRow - 1:
            row.append(True)
        else:
            horizontalRanges = [range(0, c), range(c+1, numCol)]
            verticalRanges = [range(0, r), range(r+1, numRow)]
            numbers = []
            for ran in horizontalRanges:
                nums = []
                for i in ran:
                    nums.append(trees[r][i])
                numbers.append(nums)

            for ran in verticalRanges:
                nums = []
                for i in ran:
                    nums.append(trees[i][c])
                numbers.append(nums)

            boolList = []
            for i in range(0, 4):
                boolList.append(visible(trees[r][c], numbers[i]))

            for b in boolList:
                if b:
                    row.append(True)
                    break
    visibilityChart.append(row)

print(visibilityChart)

