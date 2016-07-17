from .confirmacionMensaje import ConfirmacionMensaje
from .mensajeEnviado import MensajeEnviado
from .estadoMensaje import EstadoMensaje

class MensajeParcialmenteEnviado(EstadoMensaje):
	#Colaboradores externos
	#confirmaciones: Conjunto<ConfirmacionMensaje>
	#msg: Mensaje

	def __init__(self, unMensaje, unConjDeConfirmaciones):
		self.confirmaciones = set(unConjDeConfirmaciones)
		self.msg = unMensaje

	def puedeEliminarse(self):
		return False

	def estaPendiente(self):
		return True

	def enviarSiPendiente(self, unMensajero):
		from .campania import Campania
		from .mensaje import Mensaje
		from .grupo import Grupo
		
		receptores = self.msg.getCampania().getGrupoReceptores().getReceptores()
		
		for receptor in receptores:
			yaEnviado = False
			for conf in self.confirmaciones:
				if conf.getReceptor() == receptor:
					yaEnviado = True
					break

			if not(yaEnviado):
				confirmaciones.add(unMensajero.enviarMensajeA(self.msg, receptor))

		self.msg.setEstado(MensajeEnviado(self.msg, confirmaciones))


	def getConfirmaciones(self):
		return set(self.confirmaciones)

	def __str__(self):
		return self.msg