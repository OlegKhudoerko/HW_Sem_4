# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
#
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import uniform


def random_list(count):
    while count < 0:
        return []
    ls = [(int(uniform(1, count))) for i in range(count)]
    return ls


def non_repeating(val_ls):
    result = []
    for i in range(len(val_ls)):
        if val_ls.count(val_ls[i]) == 1:
            result.append(val_ls[i])
    return result


ls = random_list(int(input("Введите число: ")))
print(ls)
print(non_repeating(ls))
