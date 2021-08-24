
import requests
res=requests.get("https://611958717b5c0f00175920c6.mockapi.io/testw")
res=res.json()
#print(res)

#print(res[0]['data'][3]['data'][2]['data'][1]['data'][3]['data'])
def poisk(x):
    if type(x) == dict and len(x) > 1:
        for key, value in x.items():
            poisk(value)
    if type(x) == dict and len(x) == 1:
        for key, value in x.items():
            if type(value) != str:
                poisk(value)
            if type(value) == str:
                if key == "res" and value == "ok":
                    return print('The "Poisk" function has completed the search for the desired fragment:', key, ':',value)
    if type(x) == list:
        for i in range(len(x)):
            poisk(x[i])
poisk(res)
