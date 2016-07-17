#from .mensajeParcialmenteEnviado import MensajeParcialmenteEnviado
from .mensajeEnviado import MensajeEnviado
from .estadoMensaje import EstadoMensaje

class MensajeProgramado(EstadoMensaje):
	#Colaboradores externos
	#msg: Mensaje

	def __init__(self, unMensaje):
		self.msg = unMensaje

	def puedeEliminarse(self):
		return True

	def estaPendiente(self):
		return True

	def enviarSiPendiente(self, unMensajero):
		from .campania import Campania
		from .mensaje import Mensaje
		from .grupo import Grupo

		receptores = self.msg.getCampania().getGrupoReceptores().getReceptores()

		confirmaciones = set()
		for receptor in receptores:
			confirmaciones.add(unMensajero.enviarMensajeA(self.msg, receptor))

		self.msg.setEstado(MensajeEnviado(self.msg, confirmaciones))


	def getConfirmaciones(self):
		return set()

	def __str__(self):
		return self.msg