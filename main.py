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

sizeDictionaryOnlyFileSize = []
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
    sizeDictionaryOnlyFileSize.append(dict(name=dirName, size=sum(fileSizes), d=directories, f=files))

sizeDictionary = []
fileNames = []
for i in reversed(range(0, len(sizeDictionaryOnlyFileSize))):
    element = sizeDictionaryOnlyFileSize[i]
    newSize = element["size"]
    if len(element["d"]) > 0:
        for d in element["d"]:
            newSize += sizeDictionary[fileNames.index(d)]["size"]
    fileNames.append(element["name"])
    new = dict(name=element["name"], size=newSize, d=element["d"], f=element["f"])
    sizeDictionary.append(new)

sizeDictionary.reverse()

deleteSizes = []
for directory in sizeDictionary:
    if directory["size"] <= 100000:
        deleteSizes.append(directory["size"])

print(sum(deleteSizes))
