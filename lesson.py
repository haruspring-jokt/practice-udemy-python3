# from sec_6.talk import human
# from sec_6.talk import animal
# from sec_6.talk import *

# r = utils.say_twice('hello')
#
# print(r)

# print(human.sing())
# print(human.cry())
#
# print(animal.sing())
# print(animal.cry())

try:
    from sec_6 import utils
except ImportError as e:
    print(e)
    from sec_6.tools import utils

print(utils.say_twice('word'))
