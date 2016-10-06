from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazMaps import InterfazMaps
from calificacion import Calificacion

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
        baresQueCumplen=[]
        calificaciones = self.puntajes.calificaciones()
        for bar in self.Habilitados():
            if calificaciones[criterio1][bar.nombre()] >= numero1 and calificaciones[criterio2][bar.nombre()] >= numero2:
                baresQueCumplen.append(bar)
        return baresQueCumplen