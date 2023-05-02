import json
from models import Node, Owner, Car, Toll


def get_all_info():
    with open('data/all_nodes.json', 'r') as data:
        all_nodes_json = json.load(data)

    with open('data/owners.json', 'r') as data:
        owners_json = json.load(data)

    with open('data/tollStations.json', 'r') as data:
        toll_stations_json = json.load(data)

    nodes = []
    owners = []
    toll_stations = []

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

    #SAME FOR TOLL_STATIONS
    for t in toll_stations_json:
        toll = Toll(
            name=t['name'],
            toll_per_cross=t['toll_per_cross'],
            location=t['location']
        )
        toll_stations.append(toll)


    #RETURNING THE RESULT
    all_info = {"all_nodes": nodes, "owners": owners, "tollStations": toll_stations}
    return all_info
