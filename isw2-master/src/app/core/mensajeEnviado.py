from .estadoMensaje import EstadoMensaje

class MensajeEnviado(EstadoMensaje):
	#Colaboradores externos
	#confirmaciones: Conjunto<ConfirmacionMensaje>
	#msg: Mensaje

	def __init__(self, unMensaje, unConjDeConfirmaciones):
		self.confirmaciones = set(unConjDeConfirmaciones)
		self.msg = unMensaje

	def puedeEliminarse(self):
		return False

	def estaPendiente(self):
		return False

	def enviarSiPendiente(self, unMensajero):
		pass

	def getConfirmaciones(self):
		return set(self.confirmaciones)

	def __str__(self):
		return self.msg