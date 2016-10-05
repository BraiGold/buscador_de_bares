import urllib2
import json
import re
class InterfazMaps:
    def distanciaEntreDosPuntos(self,origen,destino):

        origen = re.sub(r"\s+", '+', origen)
        destino = re.sub(r"\s+", '+', destino)

        jsonAnsw = urllib2.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origen +"+CABA&destinations="+destino+"&key=AIzaSyC8qreaF3arpQGNUPzehVMZXyiUtznnRlM&mode=walking")
        parsed_json = json.loads(jsonAnsw.read())

        return parsed_json['rows'][0]['elements'][0]['distance']['value']
    
    def mostrarMapa(self,direccion):
        direccion = re.sub(r"\s+", '+', direccion)
        jsonAnsw = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+ direccion +"&key=AIzaSyCuUp-M20tNcwQxYm4V8Sp05lulzvPm9CA")
        parsed_json = json.loads(jsonAnsw.read())
        latitud = parsed_json['results'][0]['geometry']['location']['lat']
        longitud = parsed_json['results'][0]['geometry']['location']['lng']
        return "https://maps.googleapis.com/maps/api/staticmap?center="+ str(latitud) +","+ str(longitud) + "&size=640x400&markers=color:blue%7Clabel:Bar%7C" + str(latitud) +","+ str(longitud) +"&zoom=16"


"""intermap=InterfazMaps()
print intermap.mostrarMapa("Avenida Cordoba 3100")"""
