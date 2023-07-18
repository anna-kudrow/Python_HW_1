# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
#  вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


total_amount = int(input("Input amount of coins: "))
reshka = 0
orel = 1
reshka_count = 0
orel_count = 0
for i in range(total_amount):
    side_of_coin = random.randint(0, 1)
    print(side_of_coin)
    if side_of_coin == reshka:
        reshka_count += 1
    else:
        orel_count += 1 
if orel_count < reshka_count:
    print(f"You have to turn {orel_count} coins")
else:
    print(f"You have to turn {reshka_count} coins")



