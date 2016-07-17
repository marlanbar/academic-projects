import datetime
from .consola import Consola
from .uiscreen import UIScreen
from ..core.campania import Campania
from ..core.receptor import Receptor

class UIListarReceptores(UIScreen):
	def __init__(self, unMain, unUsuario, unaCampania):
		super().__init__(unMain)
		self.usuario = unUsuario
		self.campania = unaCampania
		
	def run(self):
		grupo = self.campania.getGrupoReceptores()
		receptores = grupo.getReceptores()
		aviso = self.campania.getAviso()

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("             Listar Receptores De Campaña                  ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Fecha Limite: ", self.campania.getFechaLimite().strftime("%d/%m/%Y"))
		self.consola.prnt("Nombre:       ", self.campania.getNombre())
		self.consola.prnt("Aviso:        ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("Criterio:     ", self.campania.getCriterio())
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		if len(receptores) == 0:
			self.consola.prnt("No hay Receptores.")
		else:
			self.recorrerOpciones(receptores, lambda c: c.getNombre(), False)
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("1. Agregar Receptores")
		if len(receptores) > 0: 	self.consola.prnt("2. Sacar Receptor")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver a Visualizar Campaña")
		self.consola.prnt("")

		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")


		if opt == "1":
			def callbackFn(receptores):
				for r in receptores:	grupo.agregar(r)
				self.main.setScreen(self)

			self.consola.clear()
			from .seleccionarReceptores import SeleccionarReceptores
			self.main.setScreen(SeleccionarReceptores(self.main, self.usuario, callbackFn))

		elif len(receptores) > 0 and opt == "2":
			self.consola.clear()
			receptor = self.displayColeccion(receptores, "Elija Receptor para sacar", lambda r: r.getNombre(), "Volver atrás")
			if receptor is not None: grupo.sacar(receptor)

		elif opt == "9":
			from .uivisualizarcampania import UIVisualizarCampania
			self.consola.clear()
			self.main.setScreen(UIVisualizarCampania(self.main, self.usuario, self.campania))

		else:
			self.consola.clear()


	def recorrerOpciones(self, lista, fn, showNumber = True):
		i = 1
		for l in lista:
			if showNumber:
				self.consola.prnt("%d. %s" % (i, fn(l)))
				i += 1
			else:
				self.consola.prnt("%s" % fn(l))

	def displayColeccion(self, col, pregunta, fn, noAnswerMsg = "Toda la lista"):
		opcion = -1
		lst = list(col)
		while opcion not in range(0, len(lst)):
			self.consola.prnt("===========================================================")
			self.consola.prnt(pregunta)
			self.consola.prnt("")

			self.recorrerOpciones(lst, fn)
			if noAnswerMsg is not None: self.consola.prnt("<nada> " +noAnswerMsg)

			self.consola.prnt("")
			self.consola.prnt(pregunta)
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")

			opcion = self.consola.askInput("Opcion (Enter para continuar): ")
			self.consola.clear()

			if noAnswerMsg and opcion == "": return None
			try:
				opcion = int(opcion) - 1
			except:
				pass
		return lst[opcion]