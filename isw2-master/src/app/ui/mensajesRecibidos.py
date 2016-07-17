import datetime

from .consola import Consola
from .uiscreen import UIScreen

from ..core.reloj import Reloj

class MensajesRecibidos(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario

	def run(self):
		alumnos = self.main.getSecretaria().getAlumnos(self.usuario.getAutoridad(), self.main.getReloj().getAnioCal())
		found = False
		for a in alumnos:
			if a.getNombre() == "Harry Potter":
				found = True
				confs = self.main.getMensajeroDemo().confirmacionesMsgEnviadosA(a)

				self.consola.prnt("Hay %s mensaje(s)" % len(confs))
				for c in confs:
					self.consola.prnt("")
					self.consola.prnt("================================")
					if c.huboError():
						self.consola.prnt("Intento de envio el %s - Error: %s" % (c.getFechaYTiempo().strftime("%d/%m/%Y %H:%M:%S"), c.getError()))
					else:
						self.consola.prnt("Enviado el %s" % c.getFechaYTiempo().strftime("%d/%m/%Y %H:%M:%S"))

					self.consola.prnt("--------------------------------")
					self.consola.prnt(c.getMensaje().getTexto())

				self.consola.prnt("")
				self.consola.prnt("###########################################")
				self.consola.askInput("Apriete ENTER para volver al menu anterior. ")

		#if not found:
		from .homeScreen import HomeScreen
		self.consola.clear()
		self.main.setScreen(HomeScreen(self.main, self.usuario))