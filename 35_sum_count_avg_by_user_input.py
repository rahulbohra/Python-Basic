count = 0
total = 0
average = 0

while True:
    inputNumber = raw_input('Enter a number : ')

    # Edge Cases
    if inputNumber == 'done':
        break
    if len(inputNumber) < 1:
        break

    # Logical work
    try:
        number = float(inputNumber)
    except:
        print 'Invalid Number'
        continue

    count = count + 1
    total = total + number
    print 'Count  Total\n', count, total

average = total / count
print average
