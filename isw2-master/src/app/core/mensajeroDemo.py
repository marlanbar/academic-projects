from .confirmacionMensaje import ConfirmacionMensaje
from .mensajero import Mensajero
from .reloj import Reloj

class MensajeroDemo(Mensajero):
	#Colaboradores Internos:
	#reloj: Reloj

	#Colaboradores Externos:
	#confirmaciones: Diccionario<Receptor, ConfirmacionMensaje>

	def __init__(self, unReloj):
		self.reloj = unReloj
		self.confirmaciones = dict()

	def enviarMensajeA(self, unMensaje, unReceptor):
		if not(unReceptor in self.confirmaciones):
			self.confirmaciones[unReceptor] = set()

		conf = ConfirmacionMensaje(unMensaje, unReceptor, self.reloj.getFechaYTiempo())
		self.confirmaciones[unReceptor].add(conf)
		return conf

	def confirmacionesMsgEnviadosA(self, unReceptor):
		if not(unReceptor in self.confirmaciones):
			return set()
		return set(self.confirmaciones[unReceptor])