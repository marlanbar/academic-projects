import datetime
from .consola import Consola
from .uiscreen import UIScreen
from ..core.aviso import Aviso
from ..core.usuario import Usuario
from ..core.campania import Campania
from ..core.campania import Criterio
from .uivisualizarcampania import UIVisualizarCampania


class UICrearCampania(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario
		
	def run(self):
		usuario = self.usuario
		hoy = self.main.reloj.getFecha()
		avisos = [a for a in usuario.getAvisos() if a.posteriorA(hoy)]

		if len(avisos) == 0:
			from .uicampania import UICampania
			self.consola.prnt("[ERROR] No hay avisos disponibles para crear una campaña.")
			self.main.setScreen(UICampania(self.main, self.usuario))
			return



		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Nueva Campaña                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		
		
		nombre = self.consola.askInput("* Nombre de la campaña: ")

		anio = self.main.reloj.getAnioCal()

		aviso = self.displayColeccion(avisos, "Elija el Aviso de la campaña", \
			(lambda aviso: "[%s] %s" % (aviso.getFecha(), aviso.getTexto())), None)



		self.consola.clear()
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Nueva Campaña                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Nombre: ", nombre)
		self.consola.prnt("Aviso:  ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")

		criterio = self.consola.askInput("Escriba un criterio: ")

		self.consola.clear()
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Nueva Campaña                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Nombre:   ", nombre)
		self.consola.prnt("Aviso:    ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("Criterio: ", criterio)
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")

		self.consola.prnt("A continuación, escriba la fecha límite de la campaña.")
		self.consola.prnt("Tiene que ser posterior o igual a la fecha del Aviso.")
		self.consola.prnt("")
		fechaOK = False
		fechaLimite = None
		while not fechaOK:
			inputDate = self.consola.askInput("Ingrese la fecha en formato DD/MM/YYYY: ")
			try:
				fechaLimite = datetime.datetime.strptime(inputDate, "%d/%m/%Y").date()
				if aviso.posteriorA(fechaLimite):
					self.consola.prnt("[ERROR] La fecha limite debe ser superior a la del aviso.")
				else:
					fechaOK = True
			except:
				self.consola.prnt("[ERROR] La fecha ingresada es inválida")
		
		grupo = usuario.crearGrupo("Campaña %s", nombre)
		campania = usuario.crearCampania(nombre, anio, aviso, grupo, fechaLimite, Criterio(criterio))
				
		
		def callbackFn(receptores):
			for r in receptores:	grupo.agregar(r)
			self.main.setScreen(UIVisualizarCampania(self.main, self.usuario, campania))

		self.consola.clear()
		from .seleccionarReceptores import SeleccionarReceptores
		self.main.setScreen(SeleccionarReceptores(self.main, self.usuario, callbackFn))


	def recorrerOpciones(self, lista, fn):
	    i = 1
	    for l in lista:
		      self.consola.prnt("%d. %s" % (i, fn(l)))
		      i += 1

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