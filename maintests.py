from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazDeUsuario import InterfazDeUsuario
from interfazMaps import InterfazMaps
from listaBares import ListaDeBares
from tests import Tests
db = "file.txt"
test = Tests(db)
test.testBuscarBaresCercanos()
