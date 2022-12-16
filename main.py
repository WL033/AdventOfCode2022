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
def findCommon(r1, r2, r3):
    for l1 in r1:
        for l2 in r2:
            if l1 == l2:
                for l3 in r3:
                    if l3 == l2:
                        return l1
'''
Step 2
Combine every three rucksacks
'''
priorityLetters = []
for i in range(0,len(rucksacks),3):
    priorityLetters.append(findCommon(rucksacks[i], rucksacks[i+1], rucksacks[i+2]))

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
