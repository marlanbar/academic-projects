from .autoridad import Autoridad

class Supervisor(Autoridad):
	#Colaboradores Internos
	#nombre: String

	def __init__(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre

	def puedeVisualizarInfoDeCurso(self, unCurso):
		return True

	def __str__(self):
		return self.nombre
