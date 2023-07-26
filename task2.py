digits = "0123456789ABCDEF"
num = int(input("Введите число: "))
print(f'Перевод числа при помощи hex {hex(num)}')
res = ""
while num > 0:
    res = digits[num % 16] + res
    num = num // 16
print(f'Перевод числа при помощи цикла {res}')