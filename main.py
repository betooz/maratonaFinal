import sys
import requests
import json

def main(dict):

    latitud = -21.170401
    longitud = -47.810326

    API_Keys = ['cffd036144be47edbd036144be47ed02',
    '9cac0d286c3a481dac0d286c3a881d18','33620927815c4caca20927815cacaccb',
    'f80bc2ef23044bf98bc2ef23048bf985','482af13348ac4b96aaf13348ac8b9654',
    '5535eb46f97843a4b5eb46f978a3a445','09d7ff3676f24f2597ff3676f2ef2525',
    '1b9ed679a9424d739ed679a942dd730a','7e86217bec0e42ce86217bec0ef2ce99',
    '29d0c2b003114c4790c2b003115c479c']

    respond = {
        "result": False,
        "description": "",
        "alerts": []
    }

    if(dict.get('service')):
        service = dict.get('service')
        if(service == 'Temperatura' or service == 'Velocidad' or service == 'Direccion'):
            data = requests.get("https://api.weather.com/v3/wx/forecast/daily/15day?geocode="+str(latitud)+","+str(longitud)+"&format=json&units=m&language=en-US&apiKey="+API_Keys[len(API_Keys) - 1])
            if (data.status_code == 200):
                result = data.json()
                respond["result"] = True
                #print(result)
                if(service == 'Temperatura'):
                    tempMax = result['temperatureMax']
                    tempMin = result['temperatureMin']
                    respond["description"] = {
                        "temperatureMax": tempMax,
                        "temperatureMin": tempMin
                    }
                    # print("tempMax: " + json.dumps(tempMax))
                    # print("tempMin: " + json.dumps(tempMin))
                if(service == 'Velocidad'):
                    daypart = result['daypart']
                    windspeed = daypart[0]['windSpeed']
                    #print(windspeed)
                    respond["description"] = {
                        "windSpeed": windspeed,
                    }
                if(service == 'Direccion'):
                    daypart = result['daypart']
                    windDirection = daypart[0]['windDirection']
                    #print(windDirection)
                    respond["description"] = {
                        "windDirection": windDirection,
                    }
        if(service == 'Evapotranspiración'):
            if(dict.get('TipoEvapotranspiracion')):
                tipo = dict.get('TipoEvapotranspiracion')
                url = "https://api.weather.com/v3/wx/forecast/hourly/agriculture/15day?geocode="+str(latitud)+","+str(longitud)+"&format=json&crop="+tipo+":50&units=m&apiKey="+API_Keys[len(API_Keys) - 1]
                #print(url);
                data = requests.get(url)
                if(data.status_code == 200):
                    respond["result"] = True
                    result = data.json()
                    #print(result)
                    fxcashour = result['forecasts1Hour']
                    respond["description"] = {
                        "forecastsNextHour": fxcashour,
                    }
                    #print(json.dumps(fxcashour))

    print(respond)
    if respond["result"]:
        return { "body": {"result": respond["description"]} }
    else:
        return { "body": {"error" : 'Ups! se presento un error intentalo de nuevo'}}

result = main({
    "service": 'Velocidad', #Temperatura, Evapotranspiración, Velocidad, Direccion
    "TipoEvapotranspiracion": 'corn',#coffee, corn, soybeans
})

print(result)