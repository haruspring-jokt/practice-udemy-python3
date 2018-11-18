"""
test doc
"""

animal = 'cat'


def f():
    """test func doc"""
    print(f.__name__)
    print(f.__doc__)
    # print(animal)
    # # below raises UnboundLocalError
    # # animal = 'dog'
    # print('local: ', locals())


f()

print('global: ', globals())
