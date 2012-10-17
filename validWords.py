import csv

validWords = {}

filename = 'wordlist.txt'
with open(filename) as f:
    data = f.readlines()

reader = csv.reader(data)
for row in reader:
    entry = row[0]
    temp = list(entry)
    temp.sort()
    key = ''.join(temp)
    if key in validWords:
        oldEntry = validWords[key]
        oldEntry.append(entry)
        validWords[key] = oldEntry
    else:
        validWords[key] = row

print "DONE!"
