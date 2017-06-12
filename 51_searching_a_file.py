openFile = open('sample.txt')
count = 0
for line in openFile:
    line = line.rstrip()
    if line.startswith('From:'):
        count += 1
        print line
print "Number of lines having 'From:' are :", count
