import datetime

from .consola import Consola
from .uiscreen import UIScreen
from .uicampania import UICampania

from .seleccionarReceptores import SeleccionarReceptores
from .mensajesRecibidos import MensajesRecibidos
from .ajustarReloj import AjustarReloj

from ..core.reloj import Reloj

class HomeScreen(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario

	def run(self):
		self.consola.prnt("            Ahora: %s" % self.main.getReloj().getFechaYTiempo().strftime("%d/%m/%Y %H:%M:%S"))
		self.consola.prnt("===========================================================")
		self.consola.prnt("1. Administrar campañas")
		self.consola.prnt("2. Simular el paso del tiempo")
		self.consola.prnt("3. Visualizar mensajes recibidos por el Alumno Harry Potter")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("99. Salir")
		self.consola.prnt("")

		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")
		if opt == "1":
			self.consola.clear()
			self.main.setScreen(UICampania(self.main, self.usuario))
		elif opt == "2":
			self.consola.clear()
			self.main.setScreen(AjustarReloj(self.main, self.usuario))
		elif opt == "3":
			self.consola.clear()
			self.main.setScreen(MensajesRecibidos(self.main, self.usuario))
		elif opt == "99":
			self.main.terminate()
		else:
			self.consola.clear()
