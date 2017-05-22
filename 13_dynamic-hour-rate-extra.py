try :
    hoursInput = raw_input("Enter Hours : ")
    hours = float(hoursInput)
    rateInput = raw_input("Enter Rate : ")
    rate = float(rateInput)

    if hours <= 40 :
        print hours * rate
    else :
        hoursDifference = hours - 40
        baseValue = 40 * rate
        extraValue = hoursDifference * (1.5 * rate)
        print baseValue + extraValue

except :
    print "Please enter numberic values only"
