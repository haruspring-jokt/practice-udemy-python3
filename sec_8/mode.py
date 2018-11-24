s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'r+', encoding='utf8') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
    # print('1:\n', f.read())
    # f.seek(0)
    # print('2:\n', f.read())

    # print(f.read())
