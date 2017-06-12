openFile = open('sample.txt')
count = 0
for line in openFile:
    line = line.rstrip()
    # Skip unintresting lines
    if not line.startswith('From:'):
        continue

    count += 1
    print line
print "Number of lines having 'From:' are :", count
