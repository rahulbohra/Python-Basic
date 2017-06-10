musketeersName = 'Tom Dick Harry'
print 'Three musketeers are', musketeersName

musketeer_1 = musketeersName[0:3]
print 'First musketeer :', musketeer_1

musketeer_2 = musketeersName[4:8]
print 'Second musketeer :', musketeer_2

musketeer_3 = musketeersName[9:14]
print 'Third musketeer :', musketeer_3

print "\n----------------- Special case, in case if you are not sure about the final length of the string --------------------\n"
musketeer_3 = musketeersName[9:20]
print 'Third musketeer [9:20], it should be [9:14]:', musketeer_3
