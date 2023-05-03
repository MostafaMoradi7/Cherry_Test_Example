from django.shortcuts import render
from . import funcs

information = funcs.get_all_info()


def test(request):
    msg = information['roads']
    return render(request, 'nodes.html', {"message": msg})


def main(request):
    return render(request, 'main.html')


def get_red_blue_cars(request):
    info = information['roads']
    headers = {"th1": "name", "th2": "width", "th3": "geom"}
    msg = {"info": info, "headers": headers}
    return render(request, 'nodes.html', {"message": msg})
