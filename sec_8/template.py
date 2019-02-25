import string

# s = """\
#
# Hi $name.
#
# $contents
#
# Have a good day
# """

# t = string.Template(s)
# contents = t.substitute(name='Mike', contents='How are you?')
# print(contents)


with open('email.txt', encoding='utf8') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Masayasu', contents='How are you?')
print(contents)
