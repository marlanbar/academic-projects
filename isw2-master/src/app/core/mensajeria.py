from .notificador import Notificador
from .campania import Campania
from .mensaje import Mensaje
from .usuario import Usuario

class Mensajeria(Notificador):
	#Colaboradores externos:
	#tiposMensaje: Conjunto<TipoMensaje>
	#admin: AdministradorDeSistema
	#mensajero: Mensajero
	#reloj: Reloj

	def __init__(self, unAdministrador, unMensajero, unReloj):
		self.admin = unAdministrador
		self.mensajero = unMensajero
		self.reloj = unReloj

		self.tiposMensaje = set()

	def serNotificado(self):
		self.enviarMensajesPendientes()

	def enviarMensajesPendientes(self):
		#Aca podria ponerse una restriccion segun la hora del dia 
		# (que por ejemplo no se mande entre las 10pm y las 7am)
		hoy = self.reloj.getFecha()

		print('[==Enviando mensajes pendientes==]')
		for user in self.admin.getUsuarios():
			for camp in user.getCampanias():
				if not(camp.yaFinalizo()):
					for msg in camp.getMensajes():
						if msg.antesDe(hoy):
							msg.enviarSiPendiente(self.mensajero)

	def registrarTipoMensaje(self, unTipoMensaje):
		self.tiposMensaje.add(unTipoMensaje)

	def getTiposMensaje(self):
		return set(self.tiposMensaje)