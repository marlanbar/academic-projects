import datetime


class Evaluacion():
	#Colaboradores internos:
	#eficiencia: Int
	#fecha: Datetime

	def __init__(self, eficiencia, fecha):
		self.eficiencia = eficiencia
		self.fecha = fecha

	def getFecha(self):
		return self.fecha

	def getEficiencia(self):
		return self.eficiencia
