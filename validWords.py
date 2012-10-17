import csv

class validWords:
    def __init__(self):
        self.words = {}

    def loadWords(self):
        filename = 'wordlist.txt'
        with open(filename) as f:
            data = f.readlines()
        
        #anagram words and stuff them in a dictionary (self.words)
        reader = csv.reader(data)
        for row in reader:
            entry = row[0]
            temp = list(entry)
            temp.sort()
            key = ''.join(temp)
            if key in self.words:
                oldEntry = self.words[key]
                oldEntry.append(entry)
                self.words[key] = oldEntry
               # print key + "---->" + str(oldEntry)
            else:
                self.words[key] = row
               # print key + "---->" + str(row)
