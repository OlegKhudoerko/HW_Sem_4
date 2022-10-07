# 4.* Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена, записать в файл
# полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import choice


def my_fun(k):
    if k < 1:
        return
    ls = range(0, 10)
    dd = ""
    with open("file.txt", "a") as f:
        for i in range(1, k):
            a = choice(ls)
            if a != 0:
                dd += str(a) + "*x^" + str(k-i+1) + ' ' + choice('+-') + ' '
        dd += str(choice(ls)) + ' = 0\n'
        f.write(dd)


for j in range(3):
    my_fun(int(input("Задайте степень, k = ")))
