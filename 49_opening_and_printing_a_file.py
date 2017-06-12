openFile = open('sample.txt', 'r')
print openFile
count = 0

for lines in openFile:
    count += 1
    #print lines
print 'Line Count :', count
