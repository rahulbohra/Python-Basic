count = 0
sum = 0
average = 0

# \n is used to print the data on new line.
print '\nBEFORE PROCESSING'
print 'Count = ', count
print 'Sum = ', sum
print 'Average = ', average
print '\nCount  Sum  Number'
for numbers in [1,5,6,39,91,14,2,73]:
    count = count + 1
    sum = sum + numbers
    print count, sum, numbers
average = sum / count

print '\nAFTER PROCESSING'
print 'Count = ', count
print 'Sum = ', sum
print 'Average = ', average
