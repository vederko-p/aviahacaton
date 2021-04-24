from datetime import date
import requests



# поиск по дате и направлению
def getFlightsTo(direction,date=date.today()):
    apiUrl = "https://api.rasp.yandex.net/v3.0/search/?apikey=0c83b2fa-aeb7-4b63-9cbe-a7647d183d89&from=s9600213&transport_types=plane&event=departure&format=json"
    
    allFlights = []
    parametrs = {'date':date}
    if direction:
        parametrs['to'] = direction
    
    response = requests.get(apiUrl,params=parametrs)
    
    if response.status_code==200:
        data = response.json()
        # добавление рейсов
        for f in data['segments']:
            allFlights.append({'to':f['to']['title'],
                                'departure':f['departure'],
                                'terminal':f['departure_terminal'],
                                'number':f['thread']['number']})
        return allFlights
    else:
       
        return "Ошибка"
# все рейсы на текущую дату
def getAllFlights(date=date.today()):
    apiUrl = 'https://api.rasp.yandex.net/v3.0/schedule/?apikey=0c83b2fa-aeb7-4b63-9cbe-a7647d183d89&station=s9600213&transport_types=plane&event=departure&format=json'
    
    allFlights = []

    parametrs = {'date':date}
    
    response = requests.get(apiUrl,params=parametrs)

    if response.status_code==200:
        data = response.json()
        # добавление рейсов
        for f in data['schedule']:
            to = f['thread']['title'].split(" — ")[-1]
            allFlights.append({'to':to,
                                'departure':f['departure'],
                                'terminal':f['terminal'],
                                'number':f['thread']['number']})
        return allFlights
    else:
        return "Ошибка"
# пример
print(getAllFlights())