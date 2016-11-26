def factorial(val):
    output = 1

    if val < 0:
        return output

    for i in range(2, val + 1):
        output *= i

    return output

print "Type a number: "
number = input()
print("Result: " + str(factorial(number)))
