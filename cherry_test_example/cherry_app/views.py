import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import funcs
from . import models

information = funcs.get_all_info()


def test(request):
    msg = information['roads']
    return render(request, 'nodes.html', {"message": msg})


def main(request):
    return render(request, 'main.html')


def get_red_blue_cars(request):
    info = funcs.find_all_red_and_blue_cars(information['owners'])
    return render(request, 'cars.html', {"message": info})


def register_car_owner(request):
    return render(request, 'registration.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        national_code = request.POST['national_code']
        age = request.POST['age']
        total_toll_paid = request.POST['total_toll_paid']

        # Save registration info
        owner = models.Owner(name=name, national_code=national_code, age=age, total_toll_paid=total_toll_paid, cars=[])
        cars = []
        # Save owner car info
        car_count = request.POST.get('carCount')
        if car_count is not None:
            for i in range(int(car_count)):
                car_type = request.POST.get('ownerCar[' + str(i) + '][type]')
                car_color = request.POST.get('ownerCar[' + str(i) + '][color]')
                car_length = request.POST.get('ownerCar[' + str(i) + '][length]')
                car_load_volume = request.POST.get('ownerCar[' + str(i) + '][load_volume]')
                owner_car = models.Car(cId=0, cType=car_type, color=car_color, length=car_length,
                                       load_volume=car_load_volume)
                cars.append(owner_car)

        # your code here
        else:
            print(request.POST)
        owner.cars = cars
        information['owners'].append(owner)
        return render(request, 'main.html')
    else:
        return HttpResponse("Failed to save information")


def get_old_owners_cars(request):
    cars = funcs.get_old_owners_cars(information['owners'])
    return render(request, 'cars.html', {"message": cars})


def get_heavy_cars(request):
    heavy_cars = funcs.get_heavy_cars(information)
    return render(request, 'cars.html', {"message": heavy_cars})


def call_test(request):
    nodes = information['all_nodes']
    test = []
    for n in nodes:
        print(n.get_location_dict())
    return render(request, 'cars.html', {"message": test})


def find_tolls_of_cars(request):
    return render(request, 'toll-lookup.html')


def find_tolls(request):
    if request.method == 'POST':
        car_id = int(request.POST.get('car_id', None))
        owner_name = str(request.POST.get('owner_name', None))

        if car_id:
            for owner in information['owners']:
                for car in owner.cars:
                    if car.id == car_id:
                        found = owner
                        car_ids = []
                        for c in found.cars:
                            car_ids.append(c.id)
                        return render(request, 'owners.html', {"found": found, "car_ids": car_ids})
        elif owner_name:
            for owner in information['owners']:
                if owner.name == owner_name:
                    found = owner
                    car_ids = []
                    for car in found.cars:
                        car_ids.append(car.id)
                    return render(request, 'owners.html', {"found": found, "car_ids": car_ids})

        # if no results were found, return a message
        return HttpResponse("No results found.")
    else:
        return HttpResponse("Failed!1")

