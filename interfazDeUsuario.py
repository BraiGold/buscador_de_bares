from bar import Bar
from listaBares import ListaDeBares
class InterfazDeUsuario:
    def __init__(self,db):
        self.listaDeBares = ListaDeBares(db)

    def menuInicial(self):
        print "seleccione la accion a realizar: "
        print "1. Agregar Bar "
        print "2. Dar Bar de Alta "
        print "3. Buscar bares cercanos (a menos de 400m) "
        print "4. Mostrar ubicacion de Bar "
        print "5. Filtrar bares "
        entrada = input()
        if entrada == 1:
            self.menuAgregarBar()
        if entrada == 2:
            self.menuDarBarDeAlta()
        if entrada == 3:
            self.menuBaresCercanos()
        if entrada == 4:
            self.menuMostrarBar()
        if entrada == 5:
            self.menuFiltrarBares()
        if entrada !=1 and entrada !=2 and entrada !=3:
            self.menuInicial()

    def ingresarWifi(self):
        print 'Ingrese Si, si el bar posee WiFi, en caso contrario No'
        wifi = raw_input()
        wif = -1
        if wifi == "Si":
            wif = 1
        elif wifi == "No":
            wif = 0
        else:
            self.ingresarWifi()
        return wif

    def menuAgregarBar(self):
        print "Ingrese nombre del bar "
        nombre = raw_input()
        print "Ingrese direccion (Todas las palabras separadas por espacios) "
        direcc = raw_input()
        print "Ingrese cantidad de enchufes "
        enchuf = input()
        print "Ingrese Descripcion"
        desc = raw_input()
        wifi = self.ingresarWifi()
        self.listaDeBares.agregarBar(Bar(nombre,direcc,enchuf,desc, wifi))
        self.menuInicial()

    def mostrarListaDeBares(self, lista):
        numeroDeBar=0
        for bar in lista:
            print "BAR ("+str(numeroDeBar) +"). "
            print "Nombre: "+ bar.nombre() +""
            print "Direccion"+ bar.direccion()+""
            print "Cantidad de Enchufes:"+str(bar.enchufes()) + ""
            if int(bar.wifi()) == 1:
                print "WiFi:"+"Si" + ""
            else:
                print "WiFi:"+"No" + ""
            print "Descripcion: "+bar.descripcion() +""
            numeroDeBar=numeroDeBar + 1

    def menuDarBarDeAlta(self):
        print "seleccione el numero de bar a dar de alta(-1 para salir): "
        self.mostrarListaDeBares(self.listaDeBares.inhabilitados())
        entrada=input()
        if entrada >= 0 and entrada < len(self.listaDeBares.inhabilitados()):
            self.listaDeBares.darDeAlta(self.listaDeBares.inhabilitados()[entrada])
            self.menuDarBarDeAlta()
        else:
            self.menuInicial()

    def menuBaresCercanos(self):
        print "ingrese su direccion actual: "
        direc=raw_input()
        print self.listaDeBares.buscarBaresCerca(direc)
        raw_input("toca enter para terminar")
        self.menuInicial()

    def menuMostrarBar(self):
        print "seleccione el numero de bar a mostrar su ubicacion(-1 para salir): "
        self.mostrarListaDeBares(self.listaDeBares.Habilitados())
        entrada=input()
        if entrada >= 0 and entrada < len(self.listaDeBares.Habilitados()):
            self.listaDeBares.mostarBar(self.listaDeBares.Habilitados()[entrada])
        else:
            self.menuInicial()

    def menuFiltrarBares(self):
        criterios = ["NivelWifi", "NivelRuido", "Atencion", "HigieneBanos", "CalidadComida", "Precios"]
        print "Seleccione los dos criterios por los que se filtrara(-1 para salir)"
        print "0. NivelWifi", "1. NivelRuido", "2. Atencion", "3. HigieneBanos", "4. CalidadComida", "5. Precios"
        print "Ingrese el primer criterio"
        criterio1 = input()
        filtrados = []
        if criterio1 >= 0 and criterio1 <= 5:
            print "Ingrese la cantidad de estrellas minimas para el primer criterio(entre 1 y 5)"
            valor1 = input()
            if valor1 < 1 or valor1 > 5:
                self.menuFiltrarBares()
            print "Ingrese el segundo criterio"
            criterio2 = input()
            if criterio2 >= 0 and criterio2 <= 5 and criterio2 != criterio1:
                print "Ingrese la cantidad de estrellas minimas para el segundo criterio(entre 1 y 5)"
                valor2 = input()
                if valor2 < 1 or valor2 > 5:
                    self.menuFiltrarBares()
                filtrados = self.listaDeBares.ordenarBaresPor(criterios[criterio1],valor1,criterios[criterio2],valor2)
            else:
                self.menuFiltrarBares()
        else:
            self.menuInicial()
        print "\nSeleccione un bar para mostrar su ubicacion(-1 para salir)"
        self.mostrarListaDeBares(filtrados)
        entrada = input()
        if entrada >= 0 and entrada < len(filtrados):
            self.listaDeBares.mostarBar(filtrados[entrada])
