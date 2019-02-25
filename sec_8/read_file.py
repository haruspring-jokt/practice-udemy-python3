s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'r', encoding='utf8') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

    # print(f.read())
