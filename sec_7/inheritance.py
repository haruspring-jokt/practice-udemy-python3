class Car(object):
    def run(self):
        print('boon')


class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def auto_run(self):
        print('auto soon')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
