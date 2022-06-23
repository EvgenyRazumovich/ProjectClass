class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city, km):
        print(self.name + ' Car is driving ' + city + ' ' + km)

    def chang_color(self, new_color):
        self.color = new_color


opel = Car('Opel', 'red', 1999, True)
opel.drive('Borisov', '15')
bmw = Car('bmw', 'black', 2003, False )
bmw.drive('Zhodino', '3')
bmw.chang_color('yellow')
print(bmw.color)