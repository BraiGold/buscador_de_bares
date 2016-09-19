from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazDeUsuario import InterfazDeUsuario
from interfazMaps import InterfazMaps
from listaBares import ListaDeBares
from tests import Tests
db2 = "file2.txt"
db = "file1.txt"
test1 = Tests(db2)
test1.testAgregar()
test1.testDarDeAlta()
test1.testBuscarBaresCercanos()

#test2 = Tests(db)
#test2.testGlobal()