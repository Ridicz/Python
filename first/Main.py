# 2.10
line = "a\n kotel\nsiala baba mak\n no i czesc"
tab = line.split()
print(tab.__len__())

# 2.11
word = "namaszczenie"
underscore = "_"
line = underscore.join(word)
print(line)

# 2.12
line = "mialem dziesiec lat \ngdy uslyszal o nim swiat"
words = line.split()
firstLetters = [w.__getitem__(0) for w in words]
lastLetters = [w.__getitem__(-1) for w in words]
print(firstLetters)
print(lastLetters)

# 2.13
line = "words are very unnecessary \nthey can only do harm"
words = line.split()
longWord = "".join(words)
print(longWord.__len__())

# 2.14
line = "when life is piece of shit \nwhen you look at it longestwordinthisstring"
words = line.split()
lengths = [w.__len__() for w in words]
print(max(lengths))
print(max(words, key=len))

# 2.15
line = [13, 41, 22, 5, 12, 1, 26, 31, 10, 20, 7]
bigNumber = "".join(map(str, line))
print(bigNumber)

# 2.16
line = "test string GvR and other things testGvRtest"
newLine = line.replace("GvR", "Guido van Rossum")
print(newLine)

# 2.17
line = "Sometimes i feel like i don't have a partner\nSometimes i feel like my only friend"
alphabeticalSorted = sorted(line.split())
print(alphabeticalSorted)
lengthSorted = sorted(line.split(), key=len)
print(lengthSorted)

# 2.18
number = 1023001305031509245201
count = str(number).count("0")
print(count)

# 2.19
numbers = [1, 3, 16, 65, 34, 111, 27, 123, 666, 908, 194, 505, 8]
result = ""
for s in map(str, numbers):
    if len(s) < 3:
        result += s.zfill(3)
    if len(s) == 3:
        result += s

print(result)
