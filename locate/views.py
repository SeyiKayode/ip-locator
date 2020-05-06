import requests
from django.shortcuts import render
# Create your views here.


def home(request):
    r = requests.get('http://api.ipstack.com/check?access_key=ee4233d618aa2abb48e1632262dcab65')
    data = r.json()
    context = {
        'ip': data['ip'],
        'country': data['country_name'],
        'region': data['region_name']
    }
    return render(request, 'locate/home.html', context)


