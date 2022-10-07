from django.shortcuts import render

# Create your views here.

import requests
import json

def shop(request):
    
    url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
    data = requests.get(url).text
    
    bike = json.loads(data)
    
    station = list()
    rent = list()
    for row in bike:
        station.append(row['StationName'])
        rent.append(row['AvaliableBikeCount'])
    
   
    return render(request,'shop.html',locals())
