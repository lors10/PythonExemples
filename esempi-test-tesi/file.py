
import json, datetime

# da oggetto python a formato json

dateTime = datetime.datetime.now()

x = \
{
    "id": "Richiesta 01",
    "value": "Schedulare la/e risorse sul nodo Slave One!",
    "datetime": str(dateTime)
},{
    "id": "Richiesta 02",
    "value": "Schedulare la/e risorse sul nodo Slave Two!",
    "date": str(dateTime),
}

y = json.dumps(x)

print(y)



# da formato json a oggetto "array" python

var_json = '{ "id":"Richiesta 01", "value":"Schedulare la/e risorse sul nodo Slave One!"}'

#var_json.append('{ "id":"Richiesta 02", "value":"Schedulare la/e risorse sul nodo Slave Two!"}')

array_python = json.loads(var_json)

#print(array_python)

#

array = ['{"id":"Richiesta 01","value":"Schedulare la/e risorse sul nodo Slave One!"}']

jsonVar = json.dumps(array)

print(array[0])

print(jsonVar)