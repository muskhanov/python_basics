"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = input("Введите целое положительное число n: ")
nn = n + n
nnn = nn + n
print("n + nn + nnn = ", int(n) + int(nn) + int(nnn))
