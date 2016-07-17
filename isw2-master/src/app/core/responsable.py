import datetime

from .receptor import Receptor

class Responsable(Receptor):
	#Colaboradores internos:
	#telefono: String
	#nombre: String
	#dni: String

	def __init__(self, nombre, telefono, dni):
		self.telefono = telefono
		self.nombre = nombre
		self.dni = dni

	def getTelefono(self):
		return self.telefono

	def getNombre(self):
		return self.nombre

	def getDni(self):
		return self.dni

	def __str__(self):
		return self.nombre