openFile = open("sample.txt")
for line in openFile:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    #print type(words)
    words = line.split()
    # Printing emails
    print words[1]
