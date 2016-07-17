class EstadoMensaje():
	def puedeEliminarse(self):
		raise NotImplemented("'puedeEliminarse' no fue implementado")
	def estaPendiente(self):
		raise NotImplemented("'estaPendiente' no fue implementado")
	def enviarSiPendiente(self, unMensajero):
		raise NotImplemented("'enviarSiPendiente' no fue implementado")
	def getConfirmaciones(self):
		raise NotImplemented("'getConfirmaciones' no fue implementado")