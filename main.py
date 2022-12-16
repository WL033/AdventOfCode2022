'''
Step 1
Get the inputs in an array
'''
with open('input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

'''
Step 3
Have a function that will find the commonalities between the two string values
'''
def findCommon(h1, h2):
    for i in range(len(h1)):
        if h1.find(h2[i]) != -1:
            return h2[i]

'''
Step 2
Have a function that will split up the text in half
'''
priorityLetters = []
for rucksack in rucksacks:
    halfIndex = int(len(rucksack) / 2)
    length = len(rucksack)
    firstHalf = rucksack[0:halfIndex]
    secondHalf = rucksack[halfIndex:length]
    priorityLetters.append(findCommon(firstHalf, secondHalf))

'''
Step 4
Have a function that will spit out a value
'''
def priorityValue(letter):
    lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.islower():
        return lowercaseAlphabet.index(letter) + 1
    else:
        return uppercaseAlphabet.index(letter) + 1 + 26


'''
Step 5
Print out the sum of the list of values
'''
priorityPoints = []
for priorityLetter in priorityLetters:
    priorityPoints.append(priorityValue(priorityLetter))

print(sum(priorityPoints))