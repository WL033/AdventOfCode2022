with open('input.txt', 'r') as f:
    lines = f.readlines()
    choices = [entry.strip() for entry in lines]

elfChoices = []
myChoices = []
for choice in choices:
    split = choice.split(" ")
    elfChoices.append(split[0])
    myChoices.append(split[1])

newElfChoices = []
for choice in elfChoices:
    if choice == "A":
        newElfChoices.append("X")
    elif choice == "B":
        newElfChoices.append("Y")
    else:
        newElfChoices.append("Z")


def resultPoint(c1, c2):

    moves = ["X", "Y", "Z"]
    myIndex = moves.index(c1)
    elfIndex = moves.index(c2)

    if myIndex == elfIndex:
        return 3
    elif (myIndex - elfIndex) % len(moves) == 1:
        return 6
    else:
        return 0

results = []

for i in range(len(elfChoices)):
    choicePoint = 0
    winPoint = resultPoint(myChoices[i], newElfChoices[i])
    if myChoices[i] == "X":
        choicePoint = 1
    elif myChoices[i] == "Y":
        choicePoint = 2
    elif myChoices[i] == "Z":
        choicePoint = 3

    results.append(winPoint + choicePoint)

print(sum(results))
