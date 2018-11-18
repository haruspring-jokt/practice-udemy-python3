# l = [1, 2, 3]
# i = 5
# # del l
#
# try:
#     l[0]
# except IndexError as exc:
#     print("don't worry {}".format(exc))
# except NameError as exc:
#     print(exc)
# except Exception as exc:
#     print('other: {}'.format(exc))
# else:
#     print('done')
# finally:
#     print('clean up')
#
# # print('last')


# raise IndexError('test error')


class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as e:
    print('[ERROR] This is my fault. Go next')
