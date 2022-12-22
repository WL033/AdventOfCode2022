with open('input.txt', 'r') as f:
    lines = f.readlines()
    terminal = [entry.strip() for entry in lines]

cdIndexes = []
for i in range(0, len(lines)):
    if lines[i].find("$ cd") > -1 and lines[i].find("..") == -1:
        cdIndexes.append(i)
cdIndexes.append(len(lines))
cdStrips = []
for i in range(0, len(cdIndexes) - 1):
    cdStrip = []
    for j in range(cdIndexes[i], cdIndexes[i + 1]):
        if lines[j].find("$ cd ..") == -1 and lines[j].find("$ ls") == -1:
            cdStrip.append(lines[j].strip())
    cdStrips.append(cdStrip)

processedDirectories = []
for strip in cdStrips:
    dirName = strip[0][5:]
    directories = []
    files = []
    fileSizes = []
    for element in strip:
        if element.find("dir ") > -1:
            directories.append(element[4:])
        elif element[0].isdigit():
            lastCharIndex = None
            for c in range(0, len(element)):
                if element[c].isdigit():
                    lastCharIndex = c
            fileSizes.append(int(element[0:(lastCharIndex + 1)]))
            files.append(dict(name=element[(lastCharIndex + 2):], size=int(element[0:(lastCharIndex + 1)])))
    processedDirectories.append(dict(name=dirName, size=sum(fileSizes), d=directories, f=files))

fileNames = []
for directory in processedDirectories:
    fileNames.append(directory["name"])

sizeDictionary = []
for directory in processedDirectories:
    subDirSum = 0
    if(len(directory["d"]) > 0):
        for ref in directory["d"]:
            subDirSum += processedDirectories[fileNames.index(ref)]["size"]
    sizeDictionary.append(dict(name=directory["name"], size=directory["size"] + subDirSum))

deletionSize = 0
for element in sizeDictionary:
    if element["size"] < 100000:
        deletionSize += element["size"]

print(deletionSize)

