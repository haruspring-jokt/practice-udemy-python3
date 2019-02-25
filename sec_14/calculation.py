import os


class Cal(object):

    def __init__(self, name='test'):
        self._name = name

    # テストしなくてもよいようなメソッドは無視してもOK
    @property
    def name(self):
        return self._name

    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('test')
