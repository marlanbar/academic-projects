import datetime
from .consola import Consola
from .uiscreen import UIScreen
from ..core.campania import Campania

class UIListarCampaniaEvaluable(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario
		
	def run(self):
		camps = [c for c in self.usuario.getCampanias() if c.puedeEvaluarse()]

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("              Listar Campañas Evaluables                   ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		if len(camps) == 0:
			from .uicampania import UICampania
			self.consola.prnt("No hay Campañas disponibles para evaluar.")
			self.consola.prnt("")
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")
			self.consola.askInput("Apriete ENTER para volver al menu anterior. ")

			self.consola.clear()
			self.main.setScreen(UICampania(self.main, self.usuario))
			return


		
		self.consola.prnt("Elija la campaña que quiere evaluar.")
		self.consola.prnt("")

		self.recorrerOpciones(camps, lambda c: "[%s] %s" % (c.getFechaLimite().strftime("%d/%m/%Y"), c.getNombre()))
		self.consola.prnt("<nada> Volver a Administrar Campañas")

		self.consola.prnt("")
		self.consola.prnt("Elija la campaña que quiere evaluar.")
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

				from .uievaluarcampania import UIEvaluarCampania
				self.consola.clear()
				self.main.setScreen(UIEvaluarCampania(self.main, self.usuario, camp))
			except:
				pass

				
	def recorrerOpciones(self, lista, fn):
	    i = 1
	    for l in lista:
		      self.consola.prnt("%d. %s" % (i, fn(l)))
		      i += 1