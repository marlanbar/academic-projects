import datetime
from .consola import Consola
from .uiscreen import UIScreen
from .uilistarreceptores import UIListarReceptores
from ..core.campania import Campania
from ..core.campania import Criterio

class UIVisualizarCampania(UIScreen):
	def __init__(self, unMain, unUsuario, unaCampania):
		super().__init__(unMain)
		self.campania = unaCampania
		self.usuario = unUsuario
	
	
	def run(self):
		aviso = self.campania.getAviso()

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Visualizar Campaña                        ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Fecha Limite: ", self.campania.getFechaLimite().strftime("%d/%m/%Y"))
		self.consola.prnt("Nombre:       ", self.campania.getNombre())
		self.consola.prnt("Aviso:        ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("Criterio:     ", self.campania.getCriterio())
		self.consola.prnt("[Finalizada]: ", "Si" if self.campania.yaFinalizo() else "No")
		self.consola.prnt("[Evaluada]:   ", "Si" if self.campania.yaFueEvaluada() else "No")
		if self.campania.yaFueEvaluada():
			ev = self.campania.getEvaluacion()
			self.consola.prnt("    Evaluacion:  [%s] Eficiencia: %d" % (ev.getFecha().strftime("%d/%m/%Y"), ev.getEficiencia()))

		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("1. Listar Receptores")
		self.consola.prnt("2. Listar Mensajes")
		if not(self.campania.yaFinalizo()): self.consola.prnt("3. Cambiar Criterio")
		if self.campania.puedeEliminarse(): self.consola.prnt("4. Eliminar campaña")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver a Administrar Campañas")
		self.consola.prnt("")

		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")
		
		
		if opt == "1":
			self.consola.clear()
			self.main.setScreen(UIListarReceptores(self.main, self.usuario, self.campania))

		elif opt == "2":
			self.consola.clear()
			from .visualizarMensajes import ListaMensajes
			self.main.setScreen(ListaMensajes(self.main, self.usuario, self.campania))

		elif not(self.campania.yaFinalizo()) and opt == "3":
			nuevoCriterio = self.consola.askInput("Escriba un nuevo criterio: ")
			self.campania.cambiarCriterio(Criterio(nuevoCriterio))

		elif self.campania.puedeEliminarse() and opt == "4":
			self.usuario.eliminarCampania(self.campania)
			self.usuario.eliminarGrupo(self.campania.getGrupoReceptores())

			from .uicampania import UICampania
			self.consola.clear()
			self.consola.prnt("[MSG] Campaña eliminada")
			self.main.setScreen(UICampania(self.main, self.usuario))

		elif opt == "9":
			from .uicampania import UICampania
			self.consola.clear()
			self.main.setScreen(UICampania(self.main, self.usuario))

		else:
			self.consola.clear()