'''
Write code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.

Desired Output:
0.8475
'''
text = "X-DSPAM-Confidence:    0.8475";
findWord = text.find('0.8475')
getOutput = float(text[findWord :])

print 'Position :', findWord
print 'Type of output :', type(getOutput)
print 'Our Desired output :', getOutput
