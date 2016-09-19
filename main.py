from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazDeUsuario import InterfazDeUsuario
from interfazMaps import InterfazMaps
from listaBares import ListaDeBares
db = "file.txt"
interfazDeUsuario=InterfazDeUsuario(db)
interfazDeUsuario.menuInicial()
