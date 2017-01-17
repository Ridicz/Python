import first


def insertion_sort(input_list, cmpfunc = cmp):
    for index in range(1, len(input_list)):
        currentvalue = input_list[index]
        position = index

        while position > 0 and compare_func(input_list[position - 1], currentvalue):
            input_list[position] = input_list[position - 1]
            position -= 1

        input_list[position] = currentvalue


def compare_func(a, b):
    if a > b:
        return False
    else:
        return True


alist = first.random_list(15)
print alist
insertion_sort(alist, compare_func)
print(alist)
