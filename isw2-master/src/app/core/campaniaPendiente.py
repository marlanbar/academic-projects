from .estadoCampania import EstadoCampania

class CampaniaPendiente(EstadoCampania):
	#Colaboradores externos
	#campania: Campania

	def __init__(self, unaCampania):
		self.campania = unaCampania

	def yaFinalizo(self):
		return False

	def yaFueEvaluada(self):
		return False

	def puedeEvaluarse(self):
		return False

	def finalizar(self):
		from .campania import Campania
		from .campaniaFinalizada import CampaniaFinalizada
		self.campania.setEstado(CampaniaFinalizada(self.campania))

	def evaluar(self, unaEvaluacion):
		raise Exception("La campaña está pendiente y no se puede evaluar.")

	def getEvaluacion(self):
		raise Exception("La campaña está pendiente y no tiene una evaluacion.")