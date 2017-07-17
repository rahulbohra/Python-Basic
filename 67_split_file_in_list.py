openFile = open("sample.txt")
for line in openFile:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    mainLine = line.split()
    email = mainLine[1].split("@")
    # Print domain name
    print email[1]
