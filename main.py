with open('input.txt', 'r') as f:
    lines = f.readlines()
    choices = [entry.strip() for entry in lines]

elfChoices = []
results = []
for choice in choices:
    split = choice.split(" ")
    elfChoices.append(split[0])
    results.append(split[1])

myChoices = []
for i in range(len(elfChoices)):
    if results[i] == "Y":  # draw
        myChoices.append(elfChoices[i])
    elif results[i] == "X":  # lose
        if elfChoices[i] == "A":  # rock
            myChoices.append("C")  # scissor
        elif elfChoices[i] == "B":  # paper
            myChoices.append("A")  # rock
        elif elfChoices[i] == "C":  # scissor
            myChoices.append("B")  # paper
    elif results[i] == "Z":  # win
        if elfChoices[i] == "A":  # rock
            myChoices.append("B")  # paper
        elif elfChoices[i] == "B":  # paper
            myChoices.append("C")  # scissor
        elif elfChoices[i] == "C":  # scissor
            myChoices.append("A")  # rock

points = []
for i in range(len(results)):
    resultPoints = 0
    choicePoints = 0

    if results[i] == "X":
        resultPoints = 0
    if results[i] == "Y":
        resultPoints = 3
    if results[i] == "Z":
        resultPoints = 6

    if myChoices[i] == "A":
        choicePoints = 1
    if myChoices[i] == "B":
        choicePoints = 2
    if myChoices[i] == "C":
        choicePoints = 3

    points.append(resultPoints + choicePoints)

print(sum(points))
