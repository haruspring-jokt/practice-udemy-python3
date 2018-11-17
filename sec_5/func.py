# def say_something():
#     s = 'hi'
#     return s
#
#
# f = say_something()
# print(f)


# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return "I don't know"
#     # print(color)
#
#
# result = what_is_this('blue')
# print(result)

# num: int = 10

#
# def add_num(a: int, b: int) -> int:
#     return a + b
#
#
# r = add_num('a', 'b')
#
# print(r)


# def menu(entry, drink, dessert):
#     print(entry)
#     print(drink)
#     print(dessert)
#
#
# menu(entry='beef', drink='beer', dessert='ice')


# def say_something(word, *args):
#     print(word)
#     for e in args:
#         print(e)
#
#
# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)


# def menu(entree='beef', drink='wine'):
# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }
# menu(**d)


def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)
