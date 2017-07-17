openFile = open('sample.txt')
count = 0
for line in openFile:
    line = line.rstrip()
    if line.startswith('From:'):
        count += 1
        print line
        #email = line[6:]
        #print email
print "Number of lines starts with 'From:' are :", count
