import path as path

with open('input.txt', 'r') as f:
    lines = f.readlines()
    outputs = [entry.strip() for entry in lines]

currentPath = "/root"
directories = {"/root": 0}

for output in outputs:

    if output.find("$") != -1:  # $

        if output.find("cd") != -1:  # $cd

            if output.find("..") != -1:

                currentPath = currentPath[0:currentPath.rfind("/")]

            elif output.find("/") != -1:
                currentPath = "/root"

            else:  # $ cd [dirName]
                currentPath = currentPath + "/" + output[output.find("cd") + 3:]
                directories.update({currentPath: 0})

    else:  # directory or file
        if output[0].isdigit():
            size = int(output[0:output.find(" ")])

            parsingPath = currentPath
            for i in range(0, currentPath.count("/")):
                directories[parsingPath] += size
                parsingPath = parsingPath[0:parsingPath.rfind("/")]



deletionSize = 0

for directory in directories:
    print(directory, directories[directory])
    if directories[directory] <= 100000:
        deletionSize += directories[directory]

print(deletionSize)