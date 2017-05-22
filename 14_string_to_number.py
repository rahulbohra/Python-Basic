astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
    print istr
except:
    istr = -1
    print 'String to int is not possbile in Python. Hence, istr = ', istr
