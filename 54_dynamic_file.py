fileName = raw_input('Enter a filename :')
try:
    openFile = open(fileName)
except:
    print "File cannot be open :", fileName
    exit()

count = 0
for line in openFile:
    if line.startswith('Subject:'):
        count += 1
print "There were", count, "subject lines in", fileName
