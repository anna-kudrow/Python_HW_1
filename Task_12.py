# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ_of_num = int(input("Summ of numbers: "))
product_of_num = int(input("Product of numbers: "))
num1 = 0
num2 = 0
for x in range(1,1000):
    for y in range(1,1000):
        if (x + y) == summ_of_num and x * y == product_of_num:
            num1 = x
            num2 = y
print(f"Numbers are {num1} and {num2}")

            
 