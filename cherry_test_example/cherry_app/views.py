import json
from django.shortcuts import render


def my_view(request):
    with open('myapp/data/all_nodes.json') as f1:
        all_nodes = json.load(f1)

    with open('myapp/data/owners.json') as f2:
        owners = json.load(f2)

    with open('myapp/data/tollStations.json') as f3:
        toll_stations = json.load(f3)

    # pass the data to your template context
    context = {'all_nodes': all_nodes, 'owners': owners, 'toll_stations': toll_stations}

    return render(request, 'my_template.html', context)
