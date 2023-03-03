'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 

'''
a = int(input('Введите число A: '))
b = int(input('Введите число, степень B: '))
result = 1
def multiply(a, b, result):
    if b == 0:
        return result
    b = b - 1
    result = result * a
    return multiply(a, b, result)


print(multiply(a, b, result))



'''

Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 

'''
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))


def sum(a, b):
    if b == 0:
        return a
    a = a + 1
    b = b - 1
    return sum(a, b)

print(sum(a, b))