basicRate = 10
fixedHours = 40
extraHourRate = 15

extraHours = raw_input('How many extra hours you worked had after your basic fixedHours? ')
try:
    extraHours = int(extraHours)
    print extraHours
    if extraHours > 40 :
        basicPay = basicRate * fixedHours
        extraPay = extraHourRate * extraHours
        totalPay = basicPay + extraPay
        #totalHours = fixedHours + extraHours # Need to find how to include variables in the print statements, hence commented.
        print 'Your total payment is', totalPay
except:
    print 'Instead of typing number you entered -', extraHours
