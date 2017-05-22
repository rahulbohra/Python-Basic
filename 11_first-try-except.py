number = raw_input('Enter a number to find a square : ')
try :
  actualNumber = int(number)**2
  print 'Square of the number is', actualNumber
except :
  print 'Instead of typing number you entered -', number
