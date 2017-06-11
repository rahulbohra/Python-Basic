fruit = 'banana'
print 'Fruit name :', fruit

fruitLength = len(fruit)
print 'Fruit Lenght :', fruitLength

print 'Fruit 1st Index letter :', fruit[1]

n = 3
print 'Fruit nth - 1 Index letter :', fruit[n - 1]

print "\n----------------- Print string with index numbers using WHILE loop --------------------\n"
index = 0
while index < fruitLength:
    print index, fruit[index]
    index += 1

print "\n----------------- Print string using FOR loop --------------------\n"
for letter in fruit:
    print letter

print "\n----------------- Counting letter 'a' in string using FOR loop --------------------\n"
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
print "Number of A's in fruit is", count

print len('banana')*7
