class Turno():
	#Colaboradores Internos:
  	#nombre: String

	def __init__(self, unNombre):
		self.nombre = unNombre

	def getNombre(self):
		return self.nombre

	def __str__(self):
		return self.nombre