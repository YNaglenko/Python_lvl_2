def operation_func(n):
    return n * 2


def change_list(sequence, f_operation):
    total = 0
    for i in range(len(sequence)):
        sequence[i] = f_operation(sequence[i])
        total += sequence[i]
    return total


list_a = [2, 4, 6, 8, 10, 12, 14]
print("Original list: {}".format(list_a))

new_total = change_list(list_a, operation_func)

print("Modified list: {}, Total sum: {}".format(list_a, new_total))
