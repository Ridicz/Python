import math

print("Type length: ")
length = input()

output = "|"

for i in range(1, length + 1):
    output += "....|"

output += "\n0"

for i in range(1, length + 1):
    for j in range(4 - int(math.floor(math.log(i, 10)))):
        output += " "
    output += str(i)

print(output)
