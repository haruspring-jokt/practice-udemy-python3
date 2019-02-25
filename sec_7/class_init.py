class Person(object):
    def __init__(self, name):
        self.name = name
        print('first')

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)


p = Person('Mike')
p.say_something()
