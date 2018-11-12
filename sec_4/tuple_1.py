# coding:utf-8
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 30)
print(x, y)

i = 10
j = 20
tmp = i
i = j
j = tmp

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
