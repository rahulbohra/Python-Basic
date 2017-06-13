openFile = open("sample.txt")
for line in openFile:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    #print type(words)
    print words[2]
