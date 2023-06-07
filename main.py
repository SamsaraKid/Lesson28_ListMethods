# mas = ['cat', 'cat2']
# d1 = {'animal1': 'cat1', 'animal2': 'cat2'}
#
#
# new = input('кого добавить?\n')
# mas.append(new)
#
# print(mas)
#
# mas.extend(d1.values())
# print(mas)

# cars = ['niva', 'audi', 'bmw']
#
# def addCar():
#     n = input('Что добавить?\n')
#     cars.append(n)
#     print(cars)
#
# def delCar():
#     n = input('Что удалить?\n')
#     try:
#         cars.remove(n)
#         print(cars)
#     except:
#         print('Такой нет, попробуйте другое')
#
# while True:
#     i = input('Добавить - 1, удалить - 2:\n')
#
#     if i == '1':
#         addCar()
#     elif i == '2':
#         delCar()
#     else:
#         print('Неверный ввод')


# mas = ['cat', 'dog', 'frog', 'cat']
#
# a = mas.index('frog')
# print(a)
#
# b = mas.count('cat')
# print(b)
#
#
# def f1():
#     n = input('кого удалить?\n')
#     if mas.count(n) > 0:
#         mas.remove(n)
#
#
# # f1()
#
#
# num = [2,4,63,1,213,3,534]
# let = ['asd', 'abc', 'qwe', 'q']
#
# num.sort()
# print(num)
#
# let.sort()
# print(let)

from random import randint

arr = []
for i in range(20):
    arr.append(randint(1, 100))

print(arr)
print('максимальное:', max(arr))
print('минимальное:', min(arr))