from .receptor import Receptor


class Grupo():
	#Colaboradores Internos:
	#Nombre: String
	#Anio: Int

	#Colaboradores Externos:
	#receptores: Conjunto<Receptor>

	def __init__(self, nombre, anio):
		self.nombre = nombre
		self.anio = anio
		self.receptores = set()


	def getNombre(self):
		return self.nombre

	def getAnio(self):
		return self.anio

	def agregar(self, unReceptor):
		self.receptores.add(unReceptor)

	def sacar(self, unReceptor):
		assert(unReceptor in self.receptores)
		self.receptores.remove(unReceptor)

	def getReceptores(self):
		return set(self.receptores)

	def __str__(self):
		return self.nombre