numberList = list()
while True:
    input = raw_input("Enter a number : ")
    if input == "done":
        break
    number = float(input)
    numberList.append(number)

average = sum(numberList) / len(numberList)
print "Average :", average
