from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazMaps import InterfazMaps

class ListaDeBares:
    def __init__(self,BD):
        interfazBaseDeDatos=InterfazBaseDeDatos()
        self.bD=BD
        self.habilitados=interfazBaseDeDatos.traerHabilitados(BD)
        self.enEspera=interfazBaseDeDatos.traerInhabilitados(BD)
    def agregarBar(self,bar):
        self.enEspera.append(bar)
        interfazBaseDeDatos.guardarTodos(self.bD,self.habilitados,self.enEspera)
    def darDeAlta(self,bar):
        self.enEspera.remove(bar)
        self.habilitados.append(bar)
        interfazBaseDeDatos.guardarTodos(self.bD,self.habilitados,self.enEspera)
    def buscarBaresCerca(self,direccion):
        interfazMaps=InterfazMaps()
        baresCercanos=[]
        for bar in self.habilitados:
            if interfazMaps.distanciaEntreDosPuntos(direccion,bar.direccion()) < 400 :
                baresCercanos.append(bar)
        return baresCercanos

    def inhabilitados(self):
        return self.enEspera
