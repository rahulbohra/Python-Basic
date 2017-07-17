'''
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''
scoreInput = raw_input('Enter your score : ')
try:
    score = float(scoreInput)
    if score >= 0.9:
        print 'Your grade is A'
    elif score >= 0.8:
        print 'Your grade is B'
    elif score >= 0.7:
        print 'Your grade is C'
    elif score >= 0.6:
        print 'Your grade is D'
    elif score < 0.6:
        print 'Your grade is F'
except:
    print 'Instead of typing number you entered -', scoreInput
