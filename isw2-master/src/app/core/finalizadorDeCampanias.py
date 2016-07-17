from .notificador import Notificador
from .campania import Campania
from .usuario import Usuario

class FinalizadorDeCampanias(Notificador):
	#Colaboradores externos:
	#admin: AdministradorDeSistema
	#reloj: Reloj

	def __init__(self, unAdministrador, unReloj):
		self.admin = unAdministrador
		self.reloj = unReloj

	def serNotificado(self):
		self.finalizarCampanias()

	def finalizarCampanias(self):
		print('[==Finalizando campañas==]')
		hoy = self.reloj.getFecha()
		for user in self.admin.getUsuarios():
			for camp in user.getCampanias():
				if not(camp.yaFinalizo()) and camp.antesDe(hoy):
					camp.finalizar()