'''
Open the file sample.txt and read it line by line.
When you find a line that starts with 'From:' like the following line:

  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.
'''
fileName = raw_input("Enter file name : ")
# Below line is Guardian Pattern
if len(fileName) < 1 : fileName = "sample.txt"

openFile = open(fileName)
count = 0
words = list()

for line in openFile:
	if not line.startswith("From:"):
		continue
	count += 1
	words = line.split()
	print words[1]

print "There were", count, "lines in the file with 'From:' as the first word."
