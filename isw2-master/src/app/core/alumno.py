import datetime

from .receptor import Receptor

class Alumno(Receptor):
	#Colaboradores internos:
	#fechaNac: Datetime
	#telefono: String
	#nombre: String
	#dni: String

	def __init__(self, nombre, telefono, dni, fechaNac):
		self.fechaNac = fechaNac
		self.telefono = telefono
		self.nombre = nombre
		self.dni = dni

	def getTelefono(self):
		return self.telefono

	def getNombre(self):
		return self.nombre

	def getDni(self):
		return self.dni

	def getFechaNacimiento(self):
		return self.fechaNac

	def __str__(self):
		return self.nombre