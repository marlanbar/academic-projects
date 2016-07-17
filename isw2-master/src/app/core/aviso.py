import datetime


class Aviso():
	#Colaboradores internos:
	#texto: String
	#fecha: Datetime

	def __init__(self, texto, fecha):
		self.texto = texto
		self.fecha = fecha

	def getFecha(self):
		return self.fecha

	def getTexto(self):
		return self.texto

	def posteriorA(self, fecha):
		return self.fecha > fecha

	def antesDe(self, fecha):
		return self.fecha <= fecha

	def __str__(self):
		return self.texto
