with open('input.txt', 'r') as f:
    lines = f.readlines()
    datastream = [entry.strip() for entry in lines]



def subroutine(list):
    for i in range(0, len(list) - 3):
        potential = list[i:i+4]

        for letter in potential:
            if potential.rfind(letter) > -1:
                break
            else:
                return i+3

print(subroutine(datastream))