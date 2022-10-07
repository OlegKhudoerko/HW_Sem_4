# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!

from random import choice


def sum_polynomials(file_1, file_2):
    with open(file_1) as f_1, open(file_2) as f_2:
        a, b = f_1.readlines(), f_2.readlines()
        if len(a) == len(b):
            with open('sum_file.txt', 'a') as sum:
                for i, line in enumerate(a):
                    sum.write(line[:-5] + ' + ' + b[i])
                else:
                    print("The contents of the files do not match!")


sum_polynomials('poly.txt', 'poly_2.txt')
