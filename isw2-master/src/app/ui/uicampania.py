from .consola import Consola
from .uiscreen import UIScreen
# from ..core.campania import Campania
# from ..core.reloj import Reloj
from .uicrearcampania import UICrearCampania
from .uivisualizarcampania import UIVisualizarCampania
from .uilistarcampania import UIListarCampania
from .uilistarcampaniaevaluable import UIListarCampaniaEvaluable

class UICampania(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario
	
	
	def run(self):
		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                 Administrar Campañas                      ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("1. Crear campaña")
		self.consola.prnt("2. Listar campañas")
		self.consola.prnt("3. Listar campañas evaluables")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver al Inicio")
		self.consola.prnt("")
		
		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")
		
		if opt == "1":
			self.consola.clear()
			self.main.setScreen(UICrearCampania(self.main, self.usuario))
		elif opt == "2":
			self.consola.clear()
			self.main.setScreen(UIListarCampania(self.main, self.usuario))
		elif opt == "3":
			self.consola.clear()
			self.main.setScreen(UIListarCampaniaEvaluable(self.main, self.usuario))
		elif opt == "9":
			from .homeScreen import HomeScreen
			self.consola.clear()
			self.main.setScreen(HomeScreen(self.main, self.usuario))
		else:
			self.consola.clear()