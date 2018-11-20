class Person(object):
    def __init__(self, name):
        self.name = name
        print('first')

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(5)

    def run(self, num):
        print('run ' * num)


    def __del__(self):
        print('good bye')


p = Person('Mike')
p.say_something()

del p

print('############')
