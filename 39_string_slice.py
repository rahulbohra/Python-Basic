musketeersName = 'Tom Dick Harry'
print 'Three musketeers are', musketeersName

musketeer_1 = musketeersName[0:3]
print 'First musketeer :', musketeer_1

musketeer_2 = musketeersName[4:8]
print 'Second musketeer :', musketeer_2

musketeer_3 = musketeersName[9:14]

print 'Third musketeer :', musketeer_3
print "\n----------------- Special case STARTS, in case if you are not sure about the final length of the string --------------------\n"
musketeer_3 = musketeersName[9:20]
print 'Third musketeer [9:20], it should be [9:14]:', musketeer_3

print "\n----------------- Special case ENDS, in case if you are not sure about the final length of the string --------------------\n"

firstTwoChars = musketeersName[:2]
print 'First Two characters of the string :', firstTwoChars

lastTwoChars = musketeersName[12:]
print 'Last Two characters of the string :', lastTwoChars

allChars = musketeersName[:]
print 'All characters of the string :', allChars
