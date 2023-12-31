"""Задание №5 Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
 Используйте комплексные числа для извлечения квадратного корня"""

import cmath
import math

# пример чисел для отрицательного D: a = 1, b = -6, c = 13
a = int(input("Ведите значения a = "))
b = int(input("Ведите значения b = "))
c = int(input("Ведите значения c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант = ", discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x1 = x2 = {x}")
else:
    x1 = (-b + cmath.sqrt(discr)) / (2 * a)
    x2 = (-b - cmath.sqrt(discr)) / (2 * a)

    print(f"Комплексные корни уравнения: \nx1 = {x1} \nx2 = {x2}")



