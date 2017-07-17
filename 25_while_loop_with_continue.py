while True:
    input = raw_input('>')
    # skip the current iteration and jump to the top of the loop and starts the next iteration. Hence, line 8 was not printed.
    if input[0] == '#': # here, input[0] means 1st character.
        continue
    if input == 'done':
        break
    print 'You entered -',input
print 'Out of while Loop.'
