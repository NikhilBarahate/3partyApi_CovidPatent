import requests

def Api_Connection():
    
    BASE_URL = 'https://data.covid19india.org/v4/min/data.min.json'

    resp = requests.get(BASE_URL)

    #print(resp.json())
    obj = resp.json()
    obj1 = obj.get('MH')
    obj2 = obj1.get('districts')

    #print(obj2)
    print('Pune districts Vaccinated2:',obj1['districts']['Pune']['total']['vaccinated2'])
    print(" ")
    #print(obj2.keys())

    for key, value in obj2.items():
        #print(key)
        try:
            print(key,":",value['total']['vaccinated2'])
        
        except KeyError:
            print(key,":",'NO Details..')
 

Api_Connection()