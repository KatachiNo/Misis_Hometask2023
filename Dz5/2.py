class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setyear(self, year):
        self.year = year

    def settype(self, type):
        self.type = type

    def setcolor(self, color):
        self.color = color

my_car = Car("белый", "легковой", 1999)

my_car.start()
my_car.stop()

