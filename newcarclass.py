class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print('Car make is: {}, car model is: {} car model is: {}!'.format(self.make, self.model, self.year))

car = Vehicle('Tesla', 'CyberTruck', '2022')
car.print_info()

