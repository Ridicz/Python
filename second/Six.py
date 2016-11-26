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


print "Type number of rows: "
rows = input()

print "Type number of columns"
columns = input()

output = ""

output += edge(columns) + "\n"

for i in range(rows):
    output += middle(columns) + "\n" + edge(columns) + "\n"

print output
