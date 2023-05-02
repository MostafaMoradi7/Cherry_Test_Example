from django.shortcuts import render
from . import funcs

information = funcs.get_all_info()


def test(request):
    msg = information['all_nodes']
    return render(request, 'index.html', {"message": msg})
