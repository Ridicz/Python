import math


def measure(length):
    output = "|"

    for i in range(1, length + 1):
        output += "....|"

    output += "\n0"

    for i in range(1, length + 1):
        for j in range(4 - int(math.floor(math.log(i, 10)))):
            output += " "
        output += str(i)

    return output


def edge(length):
    out = "+"

    for j in range(length):
        out += "---+"

    return out


def middle(length):
    out = "|"

    for j in range(length):
        out += "   |"

    return out


def rectangle(width, height):
    output = ""

    output += edge(width) + "\n"

    for i in range(height):
        output += middle(width) + "\n" + edge(width) + "\n"

    return output

print("Type length: ")
leng = input()
print(measure(leng))

print "Type number of rows: "
rows = input()
print "Type number of columns"
columns = input()
print(rectangle(columns, rows))
