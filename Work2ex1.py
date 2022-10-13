#Задание 1. Написать программу, считывающую список чисел и выводящую список в обратном порядке.
#Реализовать считывание из ввода любым из двухх способов:
#1. Считывается число n, затем n -е количество чисел вводится через enter;
#2. Считывать числа из одной строки через пробел.

n = int(input())
number_list = []
for i in range(n):
    number = int(input())
    number_list.append(number)
print(number_list)
number_list.reverse()
print(number_list)








