emailHeader = 'From rahulmbohra@gmail.com Sun June 11th 2017 21:48:00'
findAtTheRate = emailHeader.find('@')
print 'At The Rate is at position :', findAtTheRate

firstSpace = emailHeader.find(' ',findAtTheRate)
print 'First Space is at position :', firstSpace

domain = emailHeader[findAtTheRate + 1 : firstSpace]
print 'Domain name :', domain
