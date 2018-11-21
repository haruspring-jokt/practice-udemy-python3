class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('boon')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd = '123'):
        # self.model = model
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self.__enable_auto_run = is_enable

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

    def auto_run(self):
        print('auto soon')


tesla_car = TeslaCar('Model S')
# tesla_car.enable_auto_run = True
# print(tesla_car.__enable_auto_run)
# tesla_car._enable_auto_run = True
tesla_car.run()
# tesla_car.__enable_auto_run = 'XXXXXXXXXX'
# print(tesla_car.__enable_auto_run)

class T(object):
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)