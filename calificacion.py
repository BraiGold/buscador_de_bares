from bar import Bar
from interfazBaseDeDatos import InterfazBaseDeDatos
from random import randint

class Calificacion:

	def __init__(self, bd):
		interfazBaseDeDatos=InterfazBaseDeDatos()
		habilitados = interfazBaseDeDatos.traerHabilitados(bd)
		self.Calificaciones = {'NivelWifi': {}, 'NivelRuido': {}, 'Atencion': {}, 'HigieneBanos': {}, 'CalidadComida': {}, 'Precios': {}}
		for bar in habilitados:
			self.Calificaciones['NivelWifi'][bar.nombre()] = randint(1,5)
			self.Calificaciones['NivelRuido'][bar.nombre()] = randint(1,5)
			self.Calificaciones['Atencion'][bar.nombre()] = randint(1,5)
			self.Calificaciones['HigieneBanos'][bar.nombre()] = randint(1,5)
			self.Calificaciones['CalidadComida'][bar.nombre()] = randint(1,5)
			self.Calificaciones['Precios'][bar.nombre()] = randint(1,5)

	def calificaciones(self):
		return self.Calificaciones

	def darCalificacion(self, nombre, criterio):
		return self.Calificaciones[criterio][nombre]

	def agregarCalificacion(self, nombre):
		self.Calificaciones['NivelWifi'][nombre] = randint(1,5)
		self.Calificaciones['NivelRuido'][nombre] = randint(1,5)
		self.Calificaciones['Atencion'][nombre] = randint(1,5)
		self.Calificaciones['HigieneBanos'][nombre] = randint(1,5)
		self.Calificaciones['CalidadComida'][nombre] = randint(1,5)
		self.Calificaciones['Precios'][nombre] = randint(1,5)
		

"""db1 = "file.txt"
calif = Calificacion(db1)
print calif.darCalificacion('Uri14', 'NivelWifi')
print calif.calificaciones()
calif.agregarCalificacion('cami')
print 'distinto:'
print calif.calificaciones()"""

