'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

OUTPUT :
Invalid input
Maximum is 7
Minimum is 4

INPUT :
qw
5
6
4
7
done
'''
largest = 0
smallest = 0
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break

    if len(num) < 1:
        break

    try:
        number = int(num)

        if number > largest:
            largest = number
        else:
            smallest = number
    except:
        print 'Invalid input'
        continue


print "Maximum is", largest
print "Minimum is", smallest
