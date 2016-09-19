from bares import *

print 'Bienvenido al buscador de bares'

while 1:
    print 'Elija una de las siguientes opciones:'
    print '1-Para agregar un bar.\n2-Para buscar los bares cercanos.\n3-Para dar de alta un bar.\n9-Para salir'
    op = input()
    if op == 1:
        var = 1
        nom = 'a'
        dire = 'a'
        hora = 'a'
        calif = 1
        wifi = 1
        enchuf = 1
        ruido = 1
        com = 1
        aten = 1
        pre = 1
        banos = 1
        agregarBar( var, nom, dire, hora, calif, wifi, enchuf, ruido, com, aten, pre, banos )
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