import urllib2
import json
import re
def distanciaEntre(origen,destino):

    origen = re.sub(r"\s+", '+', origen)
    destino = re.sub(r"\s+", '+', destino)

    jsonAnsw = urllib2.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origen +"+CABA&destinations="+destino+"&key=AIzaSyC8qreaF3arpQGNUPzehVMZXyiUtznnRlM&mode=walking")
    parsed_json = json.loads(jsonAnsw.read())

    return parsed_json['rows'][0]['elements'][0]['distance']['value']


print distanciaEntre("Av. Callao 365","Av. Corrientes 2314")
