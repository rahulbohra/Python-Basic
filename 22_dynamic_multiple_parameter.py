try:
    input_1 = raw_input('Enter first number : ')
    num_1 = float(input_1)

    input_2 = raw_input('Enter second number : ')
    num_2 = float(input_2)

    def addition (a, b):
        x = a + b
        return x

    print addition(num_1, num_2)
except:
    print "Please enter numberic values only"
