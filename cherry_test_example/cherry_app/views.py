from django.shortcuts import render
from . import funcs

information = funcs.get_all_info()


def test(request):
    msg = information['roads']
    return render(request, 'index.html', {"message": msg})


def main(request):
    return render(request, 'main.html')


def get_red_blue_cars(request):
    pass