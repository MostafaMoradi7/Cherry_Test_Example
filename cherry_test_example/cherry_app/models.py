class Node:
    def __init__(self, car, location, date):
        self.car = car
        self.location = location
        self.date = date


class Owner:
    def __int__(self, name, national_code, age,
                total_toll_paid, owner_car):
        self.name = name
        self.national_code = national_code
        self.age = age
        self.total_toll_paid = total_toll_paid
        self.cars = owner_car


class Car:
    def __init__(self, cId, cType, color, length, load_volume):
        self.id = cId
        self.type = cType
        self.color = color
        self.length = length
        self.load_volume = load_volume


