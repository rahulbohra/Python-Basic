largest_number_so_far = 0
print 'Largest number before processing : ', largest_number_so_far
for numbers in [7,1,56,2,86,94,15,24]:
    if largest_number_so_far < numbers:
        largest_number_so_far = numbers
    print largest_number_so_far, numbers
print 'Largest number after processing : ', largest_number_so_far
