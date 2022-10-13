# Задание 2. Написать программу, считывающую список чисел и выводящую:
# а.минимальное число;
# б. максимальное число;
# в. среднее арифметическое чисел из списка;
# г. отсортированный список.
# Реализовать считывание из ввода любым из двухх способов:
# 1. Считывается число n, затем n -е количество чисел вводится через enter;
# 2. Считывать числа из одной строки через пробел.

import statistics
n = int(input())
number_list = []
for i in range(n):
    number = int(input())
    number_list.append(number)
print(min(number_list))
print(max(number_list))
print(statistics.fmean(number_list))
number_list.sort()
print(number_list)







