from tkinter import Entry

from django.forms import model_to_dict
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

from main.models import Weather

weatherDTO = Weather();


def index(request):
    if request.method == 'POST':
        city = request.POST['city']


        ''' api key might be expired use your own api_key 
			place api_key in place of appid ="" '''

        # source contain JSON data from API
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': str(list_of_data['weather'][0]['icon'])

        }

        weatherDTO.city = city
        weatherDTO.country_code = str(list_of_data['sys']['country'])
        weatherDTO.coordinate = str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])
        weatherDTO.temp = str(list_of_data['main']['temp']) + 'k'
        weatherDTO.pressure = str(list_of_data['main']['pressure'])
        weatherDTO.humidity = str(list_of_data['main']['humidity'])
        weatherDTO.description = str(list_of_data['weather'][0]['description'])
        weatherDTO.icon = str(list_of_data['weather'][0]['icon'])

        weatherDTO.save();

        print(weatherDTO.temp)


    else:
        data = {}
    return render(request, "main/index.html", data)


def history(request):
    if request.method == 'GET':
        allentries = Weather.objects.all()

        results = {'altpass': 'xx',
                   'altfail': 'hh',
                   }
        allentries = Weather.objects.all()

        print(allentries)
    else:
        results ={}

    return render(request, "history.html", results)