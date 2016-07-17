from .estadoCampania import EstadoCampania

import datetime

class CampaniaEvaluada(EstadoCampania):
	#Colaboradores externos
	#evaluacion: Evaluacion
	#campania: Campania

	def __init__(self, unaCampania, unaEvaluacion):
		self.evaluacion = unaEvaluacion
		self.campania = unaCampania

	def yaFinalizo(self):
		return True

	def yaFueEvaluada(self):
		return True

	def puedeEvaluarse(self):
		from .campania import Campania
		#Despues se le agrega lo de X dias de reevaluacion
		#return self.fecha > fecha
		return False

	def finalizar(self):
		pass

	def evaluar(self, unaEvaluacion):
		raise Exception("La campaña ya no puede reevaluarse.")
		#self.campania.setEstado(CampaniaEvaluada(self.campania, unaEvaluacion))

	def getEvaluacion(self):
		return self.evaluacion