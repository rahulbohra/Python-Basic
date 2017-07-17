numberList = list()
while True:
    input = raw_input("Enter a number : ")
    if input == "done": break

    try :
        number = float(input)
        numberList.append(number)
    except :
        print 'Please enter only numbers. Instead of number you have entered -', input

average = sum(numberList) / len(numberList)
print "Average :", average
