with open('input.txt', 'r') as f:
    lines = f.readlines()
    sections = [entry.strip() for entry in lines]

col1 = []
col2 = []
# Step 1: Interpret the sections into ranges
for section in sections:
     col1.append(section.split[0])
     col2.append(section.split[1])


# Have a function that will check if the ranges meet the condition for a range inside another
# 1. find the range that will contain the other
# 2. see if the min and max are inside the other min and max.
