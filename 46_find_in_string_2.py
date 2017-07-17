emailHeader = 'From rahulmbohra@gmail.com Sun June 11th 2017 21:48:00'
findAtTheRate = emailHeader.find('@')
print 'At The Rate is at position :', findAtTheRate

# Find "space" after the position (findAtTheRate), the second parameter of find()
firstSpace = emailHeader.find(' ',findAtTheRate)
print 'First Space is at position :', firstSpace

domain = emailHeader[findAtTheRate + 1 : firstSpace]
print 'Domain name :', domain

x = 'From marquard@uct.ac.za'
print x[8]
print x[14:17]

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print data[pos:pos+3]
