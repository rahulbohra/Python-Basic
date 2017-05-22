basicRate = 10
fixedHours = 40
extraHourRate = 15

extraHours = raw_input('How many extra hours you worked had after your basic fixedHours? ')
try:
    extraHours = int(extraHours)
    if extraHours > 0 :
        basicPay = basicRate * fixedHours
        extraPay = extraHourRate * extraHours
        totalPay = basicPay + extraPay
        #totalHours = fixedHours + extraHours # Need to find how to include variables in the print statements, hence commented.
        print 'Your total payment is', totalPay
    else:
        print 'Number of Hours should be greater then 0'
except:
    print 'Instead of typing number you entered -', extraHours
