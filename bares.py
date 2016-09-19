class Bar( object ):

    def __init__( self, nombre, direc, horarios, calif, wifi, enchufes, ruido, comida, atencion, precios, banos ):
        
        self.nombre = nombre
        self.direccion = direc
        self.general = calif
        self.calificacion = [ calif ]
        self.wifi = [ wifi ]
        self.enchufes = [ enchufes ]
        self.horarios = horarios
        self.ruido = [ ruido ]
        self.comida = [ comida ]
        self.atencion = [ atencion ]
        self.precios = [ precios ]
        self.banos = [ banos ]

    def mostrar( self ):

        self.mostrar = 1



aDarDeAlta = [  ]
bares = [  ]


def darDeAlta( i ):
    while 1:
        print 'Ingrese el numero de bar a dar de alta. El numero es la primera columna de la lista.\n'
        alta = input()
        if alta < i and alta > 0:
            darAlta = aDarDeAlta[alta - 1]
            darAlta.mostrar()
            bares.append(darAlta)
            aDarDeAlta.pop(alta - 1)
            print 'Se a realizado la alta con exito\n\n'
            break
        else:
            print 'La opcion seleccionada no es correcta.\n'

def agregarBar(  ):
    print 'Ha seleccionado agrega bar\nIngrese el nombre'
    nom = raw_input()

    print 'Ingrese la direccion'
    dire = raw_input()

    print 'Ingrese el horario del local'
    hora = raw_input()

    print 'Ingrese la calificacion del bar.\nLa calificacion se mide con los numeros del 1 y 5, siendo el 1, no me gusta este bar, y el 5, me encanta este bar.'
    calif = 0
    while 1:
        calif = input()
        if calif < 6 and calif > 0:
            break
        else:
            print 'La calificacion es entre 1 y 5.\nIngrese nuevamente la calificacion'
    
    print 'Ingrese el nivel del WiFi del bar.\nEl nivel de WiFi se mide con los numeros del 1 y 5, siendo el 1, bajo nivel de WiFi, y el 5, buena senal de WiFi.'
    wifi = 0
    while 1:
        wifi = input()
        if wifi < 6 and wifi > 0:
            break
        else:
            print 'El nivel de WiFi es entre 1 y 5.\nIngrese nuevamente el nivel de WiFi'
    
    print 'Ingrese la cantidad de enchufes del bar.\nLa cantidad de enchufes se mide con los numeros del 1 y 5, siendo el 1, poca cantidad de enchufes, y el 5, un enchufe o mas por mesa.'
    enchuf = 0
    while 1:
        enchuf = input()
        if enchuf < 6 and enchuf > 0:
            break
        else:
            print 'La cantidad de enchufes es entre 1 y 5.\nIngrese nuevamente la cantidad de enchufes'
    
    print 'Ingrese el nivel de ruido del bar.\nEl nivel de ruido se mide con los numeros del 1 y 5, siendo el 1, poco ruido, y el 5, mucho ruido.'
    ruido = 0
    while 1:
        ruido = input()
        if ruido < 6 and ruido > 0:
            break
        else:
            print 'El nivel de ruido es entre 1 y 5.\nIngrese nuevamente el nivel de ruido'
    
    print 'Ingrese la calidad de la comida del bar.\nLa calidad de la comida se mide con los numeros del 1 y 5, siendo el 1, la comida es muy mala, y el 5, La comida es muy rica.'
    com = 0
    while 1:
        com = input()
        if com < 6 and com > 0:
            break
        else:
            print 'La calidad de la comida es entre 1 y 5.\nIngrese nuevamente la calidad de la comida'
    
    print 'Ingrese el nivel de atencion del bar.\nEl nivel de atencion se mide con los numeros del 1 y 5, siendo el 1, la atencion es muy mala, y el 5, la atencion es muy buena.'
    aten = 0
    while 1:
        aten = input()
        if aten < 6 and aten > 0:
            break
        else:
            print 'El nivel de atencion es entre 1 y 5.\nIngrese nuevamente el nivel de atencion'

    print 'Ingrese el nivel del precio del bar.\nEl nivel del precio se mide con los numeros del 1 y 5, siendo el 1, es muy caro, y el 5, es muy barato.'
    pre = 0
    while 1:
        pre = input()
        if pre < 6 and pre > 0:
            break
        else:
            print 'El nivel del precio es entre 1 y 5.\nIngrese nuevamente el nivel del precio'

    print 'Ingrese el nivel de higiene de los banos del bar.\nEl nivel de higiene de los banos se mide con los numeros del 1 y 5, siendo el 1, el bano estaba muy suicio, y el 5, el bano estaba impecable.'
    banos = 0
    while 1:
        banos = input()
        if banos < 6 and banos > 0:
            break
        else:
            print 'El nivel de higiene de los banos es entre 1 y 5.\nIngrese nuevamente el nivel de higiene de los banos'

    bar = Bar( nom, dire, hora, calif, wifi, enchuf, ruido, com, aten, pre, banos )
    aDarDeAlta.append(bar)

    print 'Su bar ha sido agregado.\nEn los proximos dias se procesara la informacion y podra visualizarlo.\n\n'


print 'Bienvenido al bucador de bares'

while 1:
    print 'Elija una de las siguientes opciones:'
    print '1-Para agregar un bar.\n2-Para buscar los bares cercanos.\n3-Para dar de alta un bar.\n9-Para salir'
    op = input()
    if op == 1:
        agregarBar(  )
    elif op == 2:
        print 'Bares cercanos\n\n'
    elif op == 3:
        print 'Lista de bares a dar de alta\n\n'
        i = 1
        for bar in aDarDeAlta:
            print i, '  ', bar.nombre, '  ', bar.direccion, '  ', bar.horarios, '  ', bar.general
            i += 1

        while 1:
            print '\n\nElija una de los siguientes opciones.'
            print '1-Dar de alta un bar.\n2-Volver al menu anterior.'
            op2 = input()
            if op2 == 1:
                darDeAlta( i )
            elif op2 == 2:
                break
            else:
                print 'La opcion ingresada no existe.\n'

    elif op == 9:
        print 'Hasta luego'
        break
    else:
        print 'La opcion ingresada no es correcta\n.'