# Problem Statement : Print TRUE as soon as you find number 4 in a array.
result = False
print 'Result : ', result

for number in [0,1,2,3,4,5,6,7,8,9]:
    if number == 4:
        result = True
        break
    print result, number

print 'Result : ', result
