# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
from random import randint
N = int(input("Enter size of the list: "))
X = int(input("Enter number to seek: "))

list = []
for i in range(N):
    list.append(randint(0,9))
print(list)

count = 0
for i in list:
    if i == X:
        count +=1
print(f"This number occurs {count} times in the list")