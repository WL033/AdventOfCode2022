with open('input.txt', 'r') as f:
    lines = f.readlines()
    datastream = [entry.strip() for entry in lines]


def has_repeated_letters(s):
    # Create a dictionary to store the count of each letter
    letter_counts = {}

    # Iterate through each letter in the string
    for letter in s:
        # If the letter is not in the dictionary, add it with a count of 1
        if letter not in letter_counts:
            letter_counts[letter] = 1
        # If the letter is already in the dictionary, increase its count by 1
        else:
            letter_counts[letter] += 1

    # Iterate through the dictionary and check if any letters have a count greater than 1
    for letter, count in letter_counts.items():
        if count > 1:
            return True

    # If no letters have a count greater than 1, return False
    return False


def subroutine(data):
    retIndex = None
    for i in range(0, len(data) - 3):
        potential = data[i:i + 4]
        print(potential)
        if not has_repeated_letters(potential):
            return i+4



print(subroutine(datastream[0]))
