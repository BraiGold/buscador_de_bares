from __future__ import division #division, para calcular promedio
from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazMaps import InterfazMaps
from calificacion import Calificacion
from operator import itemgetter #sort

class ListaDeBares:
    def __init__(self,BD):
        interfazBaseDeDatos=InterfazBaseDeDatos()
        self.puntajes=Calificacion(BD)
        self.bD=BD
        self.habilitados=interfazBaseDeDatos.traerHabilitados(BD)
        self.enEspera=interfazBaseDeDatos.traerInhabilitados(BD)
    def agregarBar(self,bar):
        interfazBaseDeDatos=InterfazBaseDeDatos()
        self.enEspera.append(bar)
        interfazBaseDeDatos.guardarTodos(self.bD,self.habilitados,self.enEspera)
    def darDeAlta(self,bar):
        interfazBaseDeDatos=InterfazBaseDeDatos()
        self.puntajes.agregarCalificacion(bar.nombre())
        self.enEspera.remove(bar)
        self.habilitados.append(bar)
        interfazBaseDeDatos.guardarTodos(self.bD,self.habilitados,self.enEspera)
    def buscarBaresCerca(self,direccion):
        interfazMaps=InterfazMaps()
        baresCercanos=[]
        for bar in self.habilitados:
            if interfazMaps.distanciaEntreDosPuntos(direccion,bar.direccion()) < 400 and bar.wifi() == 1:
                baresCercanos.append(bar)
        return baresCercanos

    def inhabilitados(self):
        return self.enEspera

    def Habilitados(self):
        return self.habilitados

    def mostarBar(self,bar):
        interfazMap=InterfazMaps()
        print interfazMap.mostrarMapa(bar.direccion())

    def ordenarBaresPor(self, criterio1, numero1, criterio2, numero2):
        baresQueCumplen = []
        promediosBares = []
        calificaciones = self.puntajes.calificaciones()
        #print "Calificaciones" #DEBUG
        #print calificaciones #DEBUG
        for bar in self.Habilitados():
            if calificaciones[criterio1][bar.nombre()] >= numero1 and calificaciones[criterio2][bar.nombre()] >= numero2:
                baresQueCumplen.append(bar)
                promedio = ((calificaciones[criterio1][bar.nombre()]+calificaciones[criterio2][bar.nombre()])/2)
                promediosBares.append(promedio)
        #print "Promedios:" #DEBUG
        #print promediosBares #DEBUG        
        respuesta = [x for (y,x) in sorted(zip(promediosBares,baresQueCumplen),key=lambda pair: pair[0],reverse=True)]

        return respuesta