# class MainError(Exception):
#     pass
#
#
# def main():
#     # raise MainError('error')
#     x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]
#     print(x)
#
#
# if __name__ == '__main__':
#     main()


# def t():
#     for i in range(10):
#         yield i
#
#
# for i in t():
#     print(i)


# def outer_func(f):
#     print(f(10))
#
#
# def test_func(x):
#     return x * 2
#
#
# # lambda x: x * 2
#
#
# outer_func(test_func)
# outer_func(lambda x: x * 2)


# y = 'something'
# x = 1 if y else 2
# print(x)


def base(x):
    def plus(y):
        return x + y

    return plus


plus = base(10)
print(plus(10))

i = 0


def add_num():
    def plus(y):
        return i + y

    return plus


i = 10
plus = add_num()
print(plus(10))

i = 100
print(plus(30))
