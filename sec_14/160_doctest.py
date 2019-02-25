class Cal(object):
    def add_num_and_double(self, x, y):
        """Add and double
        # 対話型シェルのようにテストを書く
        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        4

        # 例外を確かめるテストの書き方
        # '...'は中略を表す
        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result


if __name__ == '__main__':
    # __main__で呼ばれたときだけテストする
    import doctest

    # doctest実行
    doctest.testmod()
