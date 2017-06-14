'''
Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
'''
fileName = raw_input("Enter the filename : ")
openFile = open(fileName)
lineList = mergeList = newList = list()
for line in openFile:
    line = line.rstrip()
    lineList = line.split()
    for word in lineList:
        if not word in newList:
            newList.append(word)
newList.sort()
print newList
