def roman2int(chosen_number):
    output = 0
    temp = 0
    prev_sign = chosen_number[0]
    for char in chosen_number[1:]:
        if translate[prev_sign] > translate[char]:
            output += translate[prev_sign] + temp
            temp = 0
        elif prev_sign == char:
            temp += translate[prev_sign]
        else:
            temp = prev_sign - temp
        prev_sign = char
    output += temp + translate[chosen_number[len(chosen_number) - 1]]
    return output


translate = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

translate = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

translate = {}
translate['I'] = 1
translate['V'] = 5
translate['X'] = 10
translate['L'] = 50
translate['C'] = 100
translate['D'] = 500
translate['M'] = 1000

print("Type a number: ")
number = raw_input()
print(roman2int(number))

