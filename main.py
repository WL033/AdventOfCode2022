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


# Have a function that will check if the ranges meet the condition for a range inside another
# 1. find the range that will contain the other
# 2. see if the min and max are inside the other min and max.

count = 0
for i in range(len(ranges1)):
    if len(ranges1[i]) > len(ranges2[i]):
        if ranges2[i][0] >= ranges1[i][0] and ranges2[i][len(ranges2[i])-1] <= ranges1[i][len(ranges1[i])-1]:
            count += 1
    elif len(ranges1[i]) < len(ranges2[i]):
        if ranges2[i][0] <= ranges1[i][0] and ranges2[i][len(ranges2[i])-1] >= ranges1[i][len(ranges1[i])-1]:
            count += 1
    elif ranges1[i] == ranges2[i]:
        count += 1


print(count)