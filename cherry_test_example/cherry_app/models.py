class Node:
    def __init__(self, car, location, date):
        self.car = car
        self.location = location
        self.date = date


class Owner:
    def __init__(self, name, national_code, age,
                 total_toll_paid, cars):
        self.name = name
        self.national_code = national_code
        self.age = age
        self.total_toll_paid = total_toll_paid
        self.cars = cars


class Car:
    def __init__(self, cId, cType, color, length, load_volume):
        self.id = cId
        self.type = cType
        self.color = color
        self.length = length
        self.load_volume = load_volume


class Toll:
    def __init__(self, name, toll_per_cross, location):
        self.name = name
        self.toll_per_cross = toll_per_cross
        self.location = location


class Road:
    def __init__(self, name, width, geom):
        self.name = name
        self.width = width
        self.geom = geom
