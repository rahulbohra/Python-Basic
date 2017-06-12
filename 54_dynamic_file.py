fileName = raw_input('Enter a filename :')
openFile = open(fileName)
count = 0
for line in openFile:
    if line.startswith('Subject:'):
        count += 1
print "There are", count, "line starts with", fileName
