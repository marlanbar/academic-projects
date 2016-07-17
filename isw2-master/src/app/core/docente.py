from .autoridad import Autoridad

class Docente(Autoridad):
	#Colaboradores Internos
	#nombre: String

	def __init__(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre

	def puedeVisualizarInfoDeCurso(self, unCurso):
		return unCurso.getDocente() == self

	def __str__(self):
		return self.nombre
