# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

number = int(input("Input a number: "))
stepen = 0
while 2 ** stepen <= number:
    print(2 ** stepen)
    stepen += 1
