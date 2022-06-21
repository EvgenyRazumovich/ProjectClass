class Car:
    def __init__(self, name_car, color, year):
        self.name_car = name_car
        self.color = color
        self.year = year


mercedes = Car(name_car='Mercedes', color='black', year=1997)
opel = Car(name_car='Opel', color='white', year=2002)
bmw = Car(name_car='BMW', color='red', year=2004)


print(mercedes.name_car, mercedes.color, mercedes.year)
print(opel.name_car, opel.color, opel.year)
print(bmw.name_car, bmw.color, bmw.year)
