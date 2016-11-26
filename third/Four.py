def fibonacci(val):
    output = -1

    if val < 0:
        return output

    a = 0
    b = 1

    for i in range(2, val + 1):
        output = a + b
        a = b
        b = output

    return output

print "Type a number: "
number = input()
print("Result: " + str(fibonacci(number)))
