# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

# def proverka():
#     while True:
#         try:
#             num = float(input("Введите число: "))
#             return num
#         except ValueError:
#             print("Вы ввели не число ! ")


# def sead(num_1):
#     suma = 0
#     for i in str(num_1):
#         if i.isdigit():
#             suma += int(i)
#     return suma


# num_1 = proverka()
# print(f"Сумма цифр= {sead(num_1)}")

#----------------------------------------------------------------

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def proverka():
#     while True:
#         try:
#             num = int(input("Введите число: "))
#             return num
#         except ValueError:
#             print("Вы ввели не число ! ")


# N = proverka()


# def proizved(N):
#     factorial = 1
#     suma = None
#     for i in range(1, N+1):
#         factorial *= i
#         suma = factorial
#     return suma


# list = []
# for j in range(1, N + 1):
#     list.append(proizved(j))

# print(f"Произведения чисел от 1 до {N}:  {list}")
# ---------------------------------------------------------------------------------

# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

# import math
# import time

# m=32768
# a=23
# b=12345

# def lin_rand_arr_flxd(seed,size):
#     if size==1:
#         return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
#     r=[0 for i in range(size)]
#     r[0]=math.ceil(seed)
#     for i in range(1,size):
#         r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
#     return r[1:size]

# print(lin_rand_arr_flxd(time.time(),1))

# --------------------------------------------------------------------------------


