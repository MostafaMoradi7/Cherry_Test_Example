import json
from django.conf import settings
import os


from .models import Node, Car, Toll, Owner, Road


def get_all_info():
    with open(os.path.join(settings.BASE_DIR, 'cherry_app', 'data/all_nodes.json'), 'r') as data1:
        all_nodes_json = json.load(data1)

    with open(os.path.join(settings.BASE_DIR, 'cherry_app', 'data/owners.json'), 'r') as data2:
        owners_json = json.load(data2)

    with open(os.path.join(settings.BASE_DIR, 'cherry_app', 'data/tollStations.json'), 'r') as data3:
        toll_stations_json = json.load(data3)

    with open(os.path.join(settings.BASE_DIR, 'cherry_app', 'data/roads.json'), 'r') as data4:
        roads_json = json.load(data4)

    nodes = []
    owners = []
    toll_stations = []
    roads = []

    # TAKING OUT ALL THE NODES IN FILE 'all_nodes.json' and saving them in cache
    for n in all_nodes_json:
        node = Node(
            car=n['car'],
            location=n['location'],
            date=n['date']
        )
        nodes.append(node)

    # TRYING TO DO THE SAME THING FOR 'owners.json'
    for o in owners_json:
        cars = []
        for c in o['ownerCar']:
            car = Car(
                cId=c['id'],
                cType=c['type'],
                color=c['color'],
                length=c['length'],
                load_volume=c['load_valume']
            )
            cars.append(car)

        owner = Owner(
            name=o['name'],
            national_code=o['national_code'],
            age=o['age'],
            total_toll_paid=o['total_toll_paid'],
            cars=cars
        )
        owners.append(owner)

    # SAME FOR TOLL_STATIONS
    for t in toll_stations_json:
        toll = Toll(
            name=t['name'],
            toll_per_cross=t['toll_per_cross'],
            location=t['location']
        )
        toll_stations.append(toll)

    # SAME FOR THE ROADS TOO
    for r in roads_json:
        road = Road(
            name=r['name'],
            geom=r['geom'],
            width=r['width']
        )
        roads.append(road)

    # RETURNING THE RESULT
    all_info = {"all_nodes": nodes, "owners": owners, "tollStations": toll_stations}
    return all_info
