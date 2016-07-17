from .confirmacionMensaje import ConfirmacionMensaje
from .mensajero import Mensajero
from .receptor import Receptor
from .mensaje import Mensaje
from .apisms import APISMS
from .reloj import Reloj


class MensajeroSMS(Mensajero):
	#Colaboradores Internos
	#reloj: Reloj
	#api: APISMS

	def __init__(self, unReloj, unaAPISMS):
		self.reloj = unReloj
		self.api = unaAPISMS

	def enviarMensajeA(self, unMensaje, unReceptor):
		(dioErr, errMsg) = self.api.enviar(unReceptor.getTelefono(), unMensaje.getTexto())

		if dioErr:
			return ConfirmacionMensaje(unMensaje, unReceptor, self.reloj.getFechaYTiempo(), errMsg)
		else:
			return ConfirmacionMensaje(unMensaje, unReceptor, self.reloj.getFechaYTiempo())