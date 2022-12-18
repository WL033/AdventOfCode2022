with open('input.txt', 'r') as f:
    lines = f.readlines()
    inputs = [entry.strip() for entry in lines]

spaceIndex = None
for i in range(len(inputs)):
    if inputs[i] == '':
        spaceIndex = i

procedures = []
for j in range(spaceIndex + 1, len(inputs)):
    procedures.append(inputs[j])

numCol = int(inputs[spaceIndex - 1][len(inputs[spaceIndex - 1]) - 1])

# Get crates in their respective arrays
rawCrates = []
for k in range(0, spaceIndex - 1):
    rawCrates.append([char for char in (lines[k].replace("\n", ''))])

cratesInCol = []
for c in range(1, numCol + 1):
    temp = []
    for r in range(0, spaceIndex - 1):
        colIndex = 4 * c - 3
        if rawCrates[r][colIndex].isalpha():
            temp.append(rawCrates[r][colIndex])
    cratesInCol.append(temp)


def move(amount, fromC, toC, list):
    destinationList = list[toC - 1]
    originalList = list[fromC - 1]
    movedLetters = []
    for l in range(0, amount):
        movedLetters.append(list[fromC - 1][l])

    for l in reversed(range(0, amount)):
        originalList.pop(l)

    for d in reversed(range(0, len(movedLetters))):
        destinationList.insert(0, movedLetters[d])

    return list


def procedureInterpreter(pText):
    global amount, fromC, toC
    count = 1
    for index in pText.split():
        if index.isdigit() and count == 1:
            amount = int(index)
            count += 1
        elif index.isdigit() and count == 2:
            fromC = int(index)
            count += 1
        elif index.isdigit() and count == 3:
            toC = int(index)
    return [amount, fromC, toC]


for procedure in procedures:
    a = procedureInterpreter(procedure)[0]
    f = procedureInterpreter(procedure)[1]
    t = procedureInterpreter(procedure)[2]
    move(a, f, t, cratesInCol)

for col in cratesInCol:
    print(col[0])
