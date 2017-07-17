number = raw_input('Enter a number to find a square : ')
try :
    # In order to accept floating numbers, we are converting the varibale to float.
    actualNumber = float(number)**2
    print 'Square of the number is', actualNumber
except :
  print 'Instead of typing number you entered -', number
