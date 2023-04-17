# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

from random import randint
N = int(input("Enter size of the list: "))
X = int(input("Enter number to seek: "))

A = [randint(0,9) for i in range(N)]

print(A)

min = abs(X - A[0])

for i in range(1, N):
    count = abs(X - A[i])
    if count < min:
        min = count

print(f"The number {X+min} is the closest to the X number")