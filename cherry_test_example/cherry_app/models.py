import re


class Node:
    def __init__(self, car, location, date):
        self.car = car
        self.location = location
        self.date = date

    def get_location_dict(self):
        srid_point = self.location.split(";")
        srid = srid_point[0].split("=")
        sr_id = srid[1]
        point_str = srid_point[1].replace("POINT (", "").replace(")", "")
        point_list = point_str.split(" ")
        point = {"x": float(point_list[0]), "y": float(point_list[1])}
        return {"SRID": sr_id, "Point": point}


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

    def get_coordinates(self):
        # Extract coordinates from geom string using regular expressions
        pattern = r'SRID=4326;MULTILINESTRING \(\((.*)\)\)'
        match = re.search(pattern, self.geom)
        if not match:
            return None

        coord_str = match.group(1)
        coord_pairs = coord_str.split(',')

        # Convert coordinate pairs to arrays of X and Y coordinates
        x_coords = []
        y_coords = []
        for pair in coord_pairs:
            x, y = map(float, pair.strip().split())
            x_coords.append(x)
            y_coords.append(y)

        return x_coords, y_coords

