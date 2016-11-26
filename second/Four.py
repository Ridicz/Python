choice = ""

while choice != "stop":
    print("Type a number: ")

    try:
        choice = raw_input()
        p = pow(float(choice), 3)
        print(choice, p)
    except ValueError:
        print("NaN!")

print("Terminating.")
