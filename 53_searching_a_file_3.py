openFile = open('sample.txt')
count = 0
for line in openFile:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    count += 1
    print line
print "Number of counts :", count
