# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

number = int(input("Input a number: "))
for i in range(0, number + 1):
    print(f"2 ^ {i} is {2 ** i}")