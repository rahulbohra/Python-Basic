# Strip of string is basically trimming the white spaces.
print '---------------------- STRIP ----------------------\n'
word = '    qwerty'
print 'Before :', word

stripWord = word.strip()
print 'After :', stripWord

print '---------------------- Left STRIP ----------------------\n'
word = '    qwerty'
print 'Before :', word

leftStripWord = word.lstrip()
print 'After :', leftStripWord

print '---------------------- Right STRIP ----------------------\n'
word = '    qwerty    '
print 'Before :', word

rightStripWord = word.rstrip()
print 'After :', rightStripWord
