from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from interfazDeUsuario import InterfazDeUsuario
from interfazMaps import InterfazMaps
from listaBares import ListaDeBares

class Tests:
	def __init__(self,BD):
		self.listaBares = ListaDeBares(BD)
		self.bd = BD

	def testAgregar(self):
		print 'Test de agregar bar.\n'
		bar0 = Bar('Barcito', 'Av. Callao 493', 4, 'El bar mas bonito.', 1)
		bar1 = Bar('Tragos', 'Araoz 1274', 2, 'Ambientes tranquilo para estudiar.', 0)
		bar2 = Bar('Hola Mundo', 'Avellaneda 621', 1, 'Todos son bienvenidos.', 1)
		bar3 = Bar('Las Tortas', 'Av. Corrientes 948', 4, 'Nuestra comida es la mejor de la ciudad.', 1)
		self.listaBares.agregarBar(bar0)
		self.listaBares.agregarBar(bar1)
		self.listaBares.agregarBar(bar2)
		self.listaBares.agregarBar(bar3)
		print 'bar 1:', bar0, '\nbar 2:', bar1, '\nbar 3:', bar2, '\nbar 4:', bar3, '\n'
		bares = self.listaBares.inhabilitados()
		i = 0
		for bar in bares:
			if i == 0 and bar == bar0:
				print 'Bar 1 se agrega correctamente.'
			elif i == 1 and bar == bar1:
				print 'Bar 2 se agrega correctamente.'
			elif i == 2 and bar == bar2:
				print 'Bar 3 se agrega correctamente.'
			elif i == 3 and bar == bar3:
				print 'Bar 4 se agrega correctamente.'
			else:
				print 'Alguno de los bares no fue agregado correctamente.'
			i += 1
		

	def testDarDeAlta(self):
		print '\n\n'
		print 'Test de dar de alta un bar.\n'
		inhab = self.listaBares.inhabilitados()
		bar0 = inhab[len(inhab)-4]
		bar2 = inhab[len(inhab)-2]
		bar3 = inhab[len(inhab)-1]
		self.listaBares.darDeAlta(bar0)
		self.listaBares.darDeAlta(bar2)
		todobien0 = 1
		todobien2 = 1
		for bar in inhab:
			if bar == bar0:
				todobien0 = 0
				print 'Bar 1 no se ha dado de alta correctamente.'
			if bar == bar2:
				todobien2 = 0
				print 'Bar 3 no se ha dado de alta correctamente.'
		if todobien0:
			print'Bar 1 habilitado no se encuentra entre los inhabilitados'
		if todobien2:
			print'Bar 3 habilitado no se encuentra entre los inhabilitados'
		hab = self.listaBares.Habilitados()
		for bar in hab:
			if bar == bar0:
				if todobien0:
					print 'Bar 1 fue habilitado correctamente'
			if bar == bar2:
				if todobien2:
					print 'Bar 3 fue habilitado correctamente'
		self.listaBares.darDeAlta(bar3)
		todobien3 = 1
		for bar in inhab:
			if bar == bar3:
				todobien3 = 0
				print 'Bar 4 no se ha dado de alta correctamente.'
		if todobien3:
			print'Bar 4 habilitado no se encuentra entre los inhabilitados'
		habi = self.listaBares.Habilitados()
		for bar in habi:
			if bar == bar3:
				if todobien3:
					print 'Bar 4 fue habilitado correctamente'

	def testBuscarBaresCercanos(self):
		habili = self.listaBares.Habilitados()
		bar0 = habili[len(habili)-3]
		print '\n\nTest de buscar bares cercanos.\n', 'Busco bares cercanos a Av. Callao 400, deberia responder solo Barcito'
		cercanos0 = self.listaBares.buscarBaresCerca('Av. Callao 400')
		print '\nLista de bares cercanos:\n', cercanos0
		if len(cercanos0) == 1 and cercanos0[0] == bar0:
			print '\nEl unico bar cercano es Barcito, por lo que busca correctamente\n'
		print 'Busco bares cerca del que no tiene WiFi, asi que deberia aparecer una lista vacia.'
		cercanos1 = self.listaBares.buscarBaresCerca('Lavalleja 1475')
		print '\nLista de bares cercanos:\n', cercanos1
		if len(cercanos1) == 0:
			print '\nNo hay bares, por lo que busca correctamente\n'
		bar4 = Bar('Nuevo', 'Honduras 4095', 1, 'Estamos cerca tuyo.', 1)
		self.listaBares.agregarBar(bar4)
		self.listaBares.darDeAlta(bar4)
		print 'Agrego un nuevo bar cerca del lugar buscado anteriormente.'
		print 'Bar 5:', bar4
		print 'Busco bares de vuelta en el mismo lugar, ahora deberia aparecer Nuevo.'
		cercanos1 = self.listaBares.buscarBaresCerca('Lavalleja 1475')
		print '\nLista de bares cercanos:\n', cercanos1
		if len(cercanos1) == 1 and cercanos1[0] == bar4:
			print '\nEl unico bar cercano es Nuevo, por lo que busca correctamente\n'
