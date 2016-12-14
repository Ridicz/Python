def flatten(sequence):
    result_sequence = list()

    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            result_sequence.extend(flatten(sequence[i]))
        else:
            result_sequence.append(sequence[i])

    return result_sequence


seq = [1, 2, (4, 5), [3, [4, 5], (7, 6, 5)], (8, 4, [2, 9])]
print("For sequence: " + str(seq) + "\nResult: " + str(flatten(seq)))
