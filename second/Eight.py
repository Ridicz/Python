firstTuple = (1, 2, 3, 4, 5, 6)
secondTuple = (1, 3, 5, 7, 9)
totalTuple = firstTuple + secondTuple

common = set()
total = set()

for i in totalTuple:
    if i not in total:
        total.add(i)
    else:
        common.add(i)

print("Values common in tuples: " + str(common))
print("Unique values in both tuples: " + str(total))
