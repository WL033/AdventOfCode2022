with open('input.txt', 'r') as f:
    lines = f.readlines()
    sections = [entry.strip() for entry in lines]

col1 = []
col2 = []
# Step 1: Interpret the sections into ranges
for section in sections:
    split = section.split(",")
    col1.append(split[0])
    col2.append(split[1])

ranges1 = []
ranges2 = []

for i in range(len(col1)):
    rangeLen = len(col1[i])
    c1split = col1[i].split("-")
    c1num1 = int(c1split[0])
    c1num2 = int(c1split[1])
    ranges1.append(range(c1num1, c1num2+1))

    c2split = col2[i].split("-")
    c2num1 = int(c2split[0])
    c2num2 = int(c2split[1])
    ranges2.append(range(c2num1, c2num2+1))


# Have a function that will check if the ranges overlap by seeing if they have any numbers that match
# 1. Find the longer range
# 2. Loop through range and see if the two ranges have the same number


def findOverlap(r1, r2):
    if(len(r1)) > len(r2):
        lRange = r1
        sRange = r2
    else:
        sRange = r2
        lRange = r1
    for num1 in lRange:
        for num2 in sRange:
            if num1 == num2:
                return True
    return False

count = 0
for i in range(len(ranges1)):
    if findOverlap(ranges1[i], ranges2[i]):
        count += 1


print(count)