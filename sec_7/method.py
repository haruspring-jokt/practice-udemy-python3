class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print(f'about human {year}')


a = Person()
# print(a)
# print(a.x)
# print(a.kind)
print(a.what_is_your_kind())

b = Person
# print(b)
# print(b.x)
# print(b.kind)
print(b.what_is_your_kind())

# Person.about()
Person.about(1990)
a.about(2000)
