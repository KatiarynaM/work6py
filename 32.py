'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума)
Input:
1, 3, 7, 10, 5, 8 - рассматриваемый список
4 - начало диапазона
8 - конец
Output:  2(7), 4(5), 5(8)'''

list = [1, 3, 7, 10, 5, 8]
min_num = int(input("Введите минимальный элемент:  "))
max_num = int(input("Введите максимальный элемент:  "))

for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        print(f'{i} ({list[i]})')
