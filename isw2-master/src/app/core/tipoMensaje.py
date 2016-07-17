class TipoMensaje():
	#Colaboradores internos:
	#nombre: String

	def __init__(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre

	def __str__(self):
		return self.nombre