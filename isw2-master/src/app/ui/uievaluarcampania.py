import datetime
from .consola import Consola
from .uiscreen import UIScreen
from ..core.campania import Campania
from ..core.evaluacion import Evaluacion

class UIEvaluarCampania(UIScreen):
	def __init__(self, unMain, unUsuario, unaCampania):
		super().__init__(unMain)
		self.usuario = unUsuario
		self.campania = unaCampania
		
	def run(self):
		aviso = self.campania.getAviso()

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                    Evaluar Campaña                        ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Fecha Limite: ", self.campania.getFechaLimite().strftime("%d/%m/%Y"))
		self.consola.prnt("Nombre:       ", self.campania.getNombre())
		self.consola.prnt("Aviso:        ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("[Evaluada]:   ", "Si" if self.campania.yaFueEvaluada() else "No")
		if self.campania.yaFueEvaluada():
			ev = self.campania.getEvaluacion()
			self.consola.prnt("    Evaluacion:  [%s] Eficiencia: %d" % (ev.getFecha().strftime("%d/%m/%Y"), ev.getEficiencia()))

		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Segun el criterio '%s', " % self.campania.getCriterio())
		self.consola.prnt("del 0 al 100, ¿qué tan eficaz cree que fue la campaña?")
		

		rta = self.consola.askInput("o presione <Enter> para cancelar la evaluacion. ")
		if rta == "":
			from .uilistarcampaniaevaluable import UIListarCampaniaEvaluable
			self.consola.clear()
			self.main.setScreen(UIListarCampaniaEvaluable(self.main, self.usuario))

		
		eficiencia = 0
		try:
			eficiencia = int(rta)
			if eficiencia < 0 or eficiencia > 100:
				self.consola.clear()
				self.consola.prnt("[ERROR] La eficiencia debe estar entre 0 y 100.")
				return
		except:
			self.consola.clear()
			return


		evaluacion = Evaluacion(eficiencia, self.main.getReloj().getFecha())
		self.campania.evaluar(evaluacion)

		from .uivisualizarcampania import UIVisualizarCampania
		self.consola.clear()
		self.main.setScreen(UIVisualizarCampania(self.main, self.usuario, self.campania))
			