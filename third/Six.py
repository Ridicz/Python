def sum_seq(sequence):
    result = 0

    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            result += sum_seq(sequence[i])
        else:
            result += sequence[i]

    return result


seq = [1, 2, (4, 5), [3, [4, 5], (7, 6, 5)], (8, 4, [2, 9])]
print("For sequence: " + str(seq) + "\nResult: " + str(sum_seq(seq)))
