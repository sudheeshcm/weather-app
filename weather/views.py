from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # Tomi's key - cb771e45ac79a4e8e2205c0ce66ff633
        # my key - 0b51d6babf4df977427294bff78d6370
        response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        res_data = json.loads(response)
        # print(json.dumps(res_data, indent=4))
        context = {
            'city': str(res_data['name'].capitalize() +', '+ res_data['sys']['country']),
            'country_code': str(res_data['sys']['country']),
            'temperature': round(int(res_data['main']['temp']) - 273.15, 2),
            'feels_like': round(int(res_data['main']['feels_like'])  - 273.15, 2),
            'max_temp':round(int(res_data['main']['temp_max']) - 273.15, 2),
            'min_temp':round(int(res_data['main']['temp_min']) - 273.15, 2),
            'description': [],
        }
        for row in res_data['weather']:
            context['description'].append(row['description'].capitalize())
    else:
        context = {}

    print(context)
    return render(request, 'index.html', context)