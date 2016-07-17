import datetime
from .consola import Consola
from .uiscreen import UIScreen
from ..core.campania import Campania

class UIListarCampania(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario
		
	def run(self):
		camps = list(self.usuario.getCampanias())

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Listar Campañas                       ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		if len(camps) == 0:
			from .uicampania import UICampania
			self.consola.prnt("No hay Campañas disponibles para editar.")
			self.consola.prnt("")
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")
			self.consola.askInput("Apriete ENTER para volver al menu anterior. ")

			self.consola.clear()
			self.main.setScreen(UICampania(self.main, self.usuario))
			return


		
		self.consola.prnt("Elija la campaña que quiere visualizar.")
		self.consola.prnt("")

		self.recorrerOpciones(camps, lambda c: "[%s] %s" % (c.getFechaLimite().strftime("%d/%m/%Y"), c.getNombre()))
		self.consola.prnt("<nada> Volver a Administrar Campañas")

		self.consola.prnt("")
		self.consola.prnt("Elija la campaña que quiere visualizar.")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")

		opcion = self.consola.askInput("Opcion (Enter para continuar): ")
		self.consola.clear()

		if opcion == "":
			from .uicampania import UICampania
			self.consola.clear()
			self.main.setScreen(UICampania(self.main, self.usuario))
		else:
			try:
				opcion = int(opcion) - 1
				camp = camps[opcion]

				from .uivisualizarcampania import UIVisualizarCampania
				self.consola.clear()
				self.main.setScreen(UIVisualizarCampania(self.main, self.usuario, camp))
			except:
				pass

				
	def recorrerOpciones(self, lista, fn):
	    i = 1
	    for l in lista:
		      self.consola.prnt("%d. %s" % (i, fn(l)))
		      i += 1