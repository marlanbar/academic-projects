from .consola import Consola
from .uiscreen import UIScreen
import datetime

class ListaMensajes(UIScreen):

	def __init__(self, unMain, unUsuario, unaCampania):
		super().__init__(unMain)
		self.usuario = unUsuario
		self.campania = unaCampania

	def run(self):
		mensajes = list(self.campania.getMensajes())
		aviso = self.campania.getAviso()

		msgDisplay = lambda m: "[%s] [%s] <%s> %s" % \
					(m.getFecha().strftime("%d/%m/%Y"), \
						"Pendiente" if m.estaPendiente() else "Enviado", \
						m.getTipoMensaje().getNombre(), \
						m.getTexto())


		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("               Listar Mensajes de Campaña                  ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Fecha Limite: ", self.campania.getFechaLimite().strftime("%d/%m/%Y"))
		self.consola.prnt("Nombre:       ", self.campania.getNombre())
		self.consola.prnt("Aviso:        ", aviso.getFecha().strftime("%d/%m/%Y"), aviso.getTexto())
		self.consola.prnt("Criterio:     ", self.campania.getCriterio())
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		if len(mensajes) == 0:
			self.consola.prnt("No hay Mensajes.")
		else:
			self.recorrerOpciones(mensajes, msgDisplay, False)
		self.consola.prnt("")
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("1. Agregar Mensaje")
		if len(mensajes) > 0: 	self.consola.prnt("2. Seleccionar Mensaje")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver a Visualizar Campaña")
		self.consola.prnt("")

		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")


		if opt == "1":
			self.agregarMensaje()

		elif len(mensajes) > 0 and opt == "2":
			self.consola.clear()
			mensaje = self.displayColeccion(mensajes, "Elija Mensaje para visualizar en detalle", msgDisplay, "Volver atrás")
			if mensaje is not None:
				from .visualizarEstadoMensaje import VisualizarEstadoMensaje
				self.consola.clear()
				self.main.setScreen(VisualizarEstadoMensaje(self.main, self.usuario, self.campania, mensaje))

		elif opt == "9":
			from .uivisualizarcampania import UIVisualizarCampania
			self.consola.clear()
			self.main.setScreen(UIVisualizarCampania(self.main, self.usuario, self.campania))

		else:
			self.consola.clear()


	def agregarMensaje(self):
		tipoMsg = self.main.getMensajeria().getTiposMensaje()

		self.consola.clear()
		if len(tipoMsg) == 0:
			self.consola.prnt("[ERROR] No hay Tipos de Mensaje disponibles para crear un mensaje.")
			return

		self.consola.prnt("")
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("                   Agregar Mensaje                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		tipoMensaje = self.displayColeccion(tipoMsg, "Elija el Tipo de Mensaje", \
			lambda t: t.getNombre(), None)

		
		self.consola.clear()
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("                   Agregar Mensaje                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Tipo de Mensaje:  ", tipoMensaje.getNombre())
		self.consola.prnt("")

		txtMsg = self.consola.askInput("Inserte texto del mensaje: ")



		self.consola.clear()
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("                   Agregar Mensaje                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Tipo de Mensaje:  ", tipoMensaje.getNombre())
		self.consola.prnt("Texto:            ", txtMsg)
		self.consola.prnt("")

		fechaLimite = self.campania.getFechaLimite()
		hoy = self.main.getReloj().getFecha()
		self.consola.prnt("A continuación, escriba la fecha del mensaje.")
		self.consola.prnt("Tiene que ser previa a la de la campaña (%s)." % \
				fechaLimite.strftime("%d/%m/%Y"))
		self.consola.prnt("y posterior a la fecha actual (%s)." % \
				hoy.strftime("%d/%m/%Y"))
		self.consola.prnt("")
		fechaOK = False
		fechaMsg = None
		while not fechaOK:
			inputDate = self.consola.askInput("Ingrese la fecha en formato DD/MM/YYYY: ")
			try:
				fechaMsg = datetime.datetime.strptime(inputDate, "%d/%m/%Y").date()
				if fechaMsg >= fechaLimite:
					self.consola.prnt("[ERROR] La fecha del mensaje debe estar antes que la de la campaña.")
				else:
					if hoy >= fechaMsg:
						self.consola.prnt("[ERROR] La fecha del mensaje debe ser posterior a la fecha actual.")
					else:
						fechaOK = True
			except:
				self.consola.prnt("[ERROR] La fecha ingresada es inválida")



		self.consola.clear()
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("                   Agregar Mensaje                         ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Tipo de Mensaje:  ", tipoMensaje.getNombre())
		self.consola.prnt("Texto:            ", txtMsg)
		self.consola.prnt("Fecha:            ", fechaMsg.strftime("%d/%m/%Y"))
		self.consola.prnt("")

		self.campania.agregarMensaje(txtMsg, tipoMensaje, fechaMsg)
		self.consola.askInput("Mensaje agregado! Toque Enter para continuar...")

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