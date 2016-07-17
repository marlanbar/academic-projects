import datetime


class ConfirmacionMensaje():
	#Colaboradores internos:
	#tuvoError: Bool
	#fechaYTiempo: Datetime
	#error: String

	#Colaboradores externos:
	#receptor: Receptor
	#mensaje: Mensaje

	def __init__(self, unMensaje, unReceptor, unaFechaYTiempo, msgError = None):
		self.receptor = unReceptor
		self.mensaje = unMensaje
		self.fechaYTiempo = unaFechaYTiempo

		if msgError is None:
			self.tuvoError = False
			self.error = ""
		else:
			self.tuvoError = True
			self.error = msgError

	def getMensaje(self):
		return self.mensaje

	def getReceptor(self):
		return self.receptor

	def getFechaYTiempo(self):
		return self.fechaYTiempo

	def huboError(self):
		return self.tuvoError

	def getError(self):
		return self.error
	def __str__(self):
		return self.mensaje