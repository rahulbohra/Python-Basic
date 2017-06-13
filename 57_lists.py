# Lists in Python. Array in PHP.
# Normal Lists
names = ["Tom", "Dick", "Harry"]
print names

print "\n"
# Multiple Lists
people = ["Kiwi", ["Nanu", "Nani"], "Mama"]
print people

print "\n"
# Using FOR Loop 1
countdown = [10,9,8,7,6,5,4,3,2,1,0]
for time in countdown:
    print time
print "Lift off!"

print "\n"
# Using FOR Loop 2
for friend in names:
    print "Hello", friend
print "Welcome Aboard!"

print "\n"
# Lists - Index value
print people[1]

print "\n"
# Changing the Lists x-index value
print "Before Changing :", people
people[0] = "Kiwi Dakri"
print "After Changing :", people

print "\n"
# Number of Elements in lists
print "Number of elements for lists countdown is : ", len(countdown)

print "\n"
# range() function applied in lists
# Below code will print lists starting from 0 till 6 like : [0, 1, 2, 3, 4, 5, 6,]
print range(7)

print "\n"
# Using len() function inside range() function
print range(len(people))

print "\n"
# range() function using FOR loop
for i in range(len(names)):
    friend = names[i]
    print "Hello", friend

print "Welcome Aboard!\n"
