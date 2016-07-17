from .estadoCampania import EstadoCampania

class CampaniaFinalizada(EstadoCampania):
	#Colaboradores externos
	#campania: Campania

	def __init__(self, unaCampania):
		self.campania = unaCampania

	def yaFinalizo(self):
		return True

	def yaFueEvaluada(self):
		return False

	def puedeEvaluarse(self):
		return True

	def finalizar(self):
		pass

	def evaluar(self, unaEvaluacion):
		from .campania import Campania
		from .campaniaEvaluada import CampaniaEvaluada
		self.campania.setEstado(CampaniaEvaluada(self.campania, unaEvaluacion))

	def getEvaluacion(self):
		raise Exception("La campaña está finalizada y no tiene una evaluacion.")