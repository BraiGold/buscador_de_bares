from bar import Bar

class InterfazBaseDeDatos:
    def traerTodos( self,file, habil ):
        bares=[]
        f = open(file,'r')
        for line in f:
            linea = line.split('--')
            nombre = linea[0]
            direccion = linea[1]
            enchufes = linea[2]
            descripcion = linea[3]
            habilitado = linea[4]
            if habilitado == habil:
                bar = Bar( nombre, direccion, enchufes, descripcion )
                bares.append(bar)
        return bares


    def traerHabilitados(self, file ):
        return self.traerTodos(file, 1)


    def traerInhabilitados(self, file ):
        return self.traerTodos(file, 0)

    def guardarInFile(self, f, bares, habil):
        for item in bares:
            f.write(item.nombre())
            f.write("--")
            f.write(item.direccion())
            f.write("--")
            f.write(str(item.enchufes()))
            f.write("--")
            f.write(item.descripcion())
            f.write("--")
            if habil == 0:
                f.write("0")
            else:    
                f.write("1")
            f.write("\n");


    def guardarTodos( self,file, baresH, baresIn):
        f = open(file, 'wb')
        f.seek(0)
        f.truncate()
        self.guardarInFile( f, baresH, 1)
        self.guardarInFile( f, baresIn, 0)
