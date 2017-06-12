'''
Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.

Desired output:
Average spam confidence: 0.750718518519
'''
fileName = raw_input("Enter file name: ")
try:
    openFile = open(fileName)
except:
    print "File does not exits :", fileName
    exit()

count = floatingSum = floatingPoint = 0.0
for line in openFile:
    if not line.startswith("X-DSPAM-Confidence:") :
       	continue

    colon = line.find(':')
    floatingPointData = line[colon+1:]
    floatingPoint = floatingPointData.lstrip()
    floatingNumber = float(floatingPoint)
    #print floatingPoint
    #print type(floatingPoint)
    #exit()

    floatingSum += floatingNumber
    count += 1
avg =  floatingSum / count
print "Average spam confidence:", avg
