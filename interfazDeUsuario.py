from bar import Bar
from listaBares import ListaDeBares
class InterfazDeUsuario:
    def __init__(self,db):
        self.listaDeBares = ListaDeBares(db)

    def menuInicial(self):
        print "seleccione la accion a realizar: /n"
        print "1. Agregar Bar /n"
        print "2. Dar Bar de Alta /n"
        print "3. Buscar bares cercanos (a menos de 400m) /n"
        entrada = input()
        if entrada == 1:
            self.menuAgregarBar()
        if entrada == 2:
            self.menuDarBarDeAlta()
        if entrada == 3:
            self.menuBaresCercanos()
        if entrada !=1 and entrada !=2 and entrada !=3:
            self.menuInicial()

    def menuAgregarBar(self):
        print "Ingrese nombre del bar "
        nombre = raw_input()
        print "Ingrese direccion (Todas las palabras separadas por espacios) "
        direcc = raw_input()
        print "Ingrese cantidad de enchufes "
        enchuf = input()
        print "Ingrese Descripcion"
        desc = raw_input()
        self.listaDeBares.agregarBar(Bar(nombre,direcc,enchuf,desc))

    def menuDarBarDeAlta(self):
        print "seleccione el numero de bar a dar de alta(-1 para salir): /n"
        numeroDeBar=0
        for bar in self.listaDeBares.inhabilitados():
            print str(i) +". "
            print "Nombre: "+ bar.nombre() +""
            print "Direccion"+ bar.direccion()+""
            print "Cantidad de Enchufes:"+bar.enchufes() + ""
            print "Descripcion"+bar.descripcion() +""
            numeroDeBar=numeroDeBar + 1
        entrada=input()
        if entrada >= 0:
            self.listaDeBares.DarDeAlta(self.listaDeBares.inhabilitados()[numeroDeBar])
        else:
            self.menuInicial()

    def menuBaresCercanos(self):
        print "ingrese su direccion actual: /n"
        direc=raw_input()
        print self.listaDeBares.buscarBaresCerca(direc)
