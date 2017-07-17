'''
Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case.
'''
fileName = raw_input('Enter file name : ')
openFile = open(fileName)
readFile = openFile.read().upper().strip()
print readFile
