'''Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент(a1), 
разность(d) и количество элементов(n) нужно ввести с клавиатуры. Формула для получения n-го 
члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

first_num = int(input("Введите первый элемент прогрессии:  "))
difference = int(input("Введите разность прогрессии:  "))
count_elements = int(input("Введите количество елементов прогрессии:  "))
arithmetic_progression = [first_num]
i = 1
while i < count_elements:
    arithmetic_progression.append(first_num + (i) * difference)
    i+=1
print(arithmetic_progression)
