with open('input.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

calories_sum = []
current_sum = 0
for calorie in calories:
    if calorie != '':
        current_sum += int(calorie)
    elif calorie == '':
        calories_sum.append(current_sum)
        current_sum = 0
calories_sum.append(current_sum)

calories_sum.sort()

print(sum(calories_sum[-3:]))
