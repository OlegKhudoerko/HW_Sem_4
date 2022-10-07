# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

def prime_factors(count):
    i = 2
    ls = []
    while count > 1:
        if count % i == 0:
            ls.append(i)
            count //= i
        else:
            i += 1
    return ls


N = int(input("Задайте натуральное число N = "))
print(prime_factors(N))
