from .consola import Consola
from .uiscreen import UIScreen

class VisualizarEstadoMensaje(UIScreen):
	
	def __init__(self, unMain, unUsuario, unaCampania, unMensaje):
		super().__init__(unMain)
		self.campania = unaCampania
		self.usuario = unUsuario
		self.mensaje = unMensaje

	def run(self):
		confirmaciones = self.mensaje.getConfirmaciones()

		self.consola.prnt("")
		self.consola.prnt("===========================================================")
		self.consola.prnt("                     Visualizar Mensaje                    ")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("Tipo de Mensaje:  ", self.mensaje.getTipoMensaje().getNombre())
		self.consola.prnt("Texto:            ", self.mensaje.getTexto())
		self.consola.prnt("Fecha:            ", self.mensaje.getFecha().strftime("%d/%m/%Y"))
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		if len(confirmaciones) == 0:
			self.consola.prnt("No hay confirmaciones del mensaje.")
		else:
			self.consola.prnt("Hay %d confirmacione(s) del mensaje." % len(confirmaciones))
			for c in confirmaciones:
				if c.huboError():
					self.consola.prnt("[%s] Intento de envio a %s - Error: %s" % \
							(c.getFechaYTiempo().strftime("%d/%m/%Y"), c.getReceptor().getNombre(), c.getError()))
				else:
					self.consola.prnt("[%s] Enviado a %s" % \
							(c.getFechaYTiempo().strftime("%d/%m/%Y"), c.getReceptor().getNombre()))
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("")
		self.consola.prnt("")
		self.consola.prnt("-----------------------------------------------------------")
		if self.mensaje.puedeEliminarse():
			self.consola.prnt("1. Eliminar Mensaje")
			self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver a Listar Mensajes de Campaña")
		self.consola.prnt("")


		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")

		if self.mensaje.puedeEliminarse() and opt == "1":
			self.campania.sacarMensaje(self.mensaje)
			
			self.consola.clear()
			from .visualizarMensajes import ListaMensajes
			self.main.setScreen(ListaMensajes(self.main, self.usuario, self.campania))

		elif opt == "9":
			self.consola.clear()
			from .visualizarMensajes import ListaMensajes
			self.main.setScreen(ListaMensajes(self.main, self.usuario, self.campania))


		if False:
			while True:
				self.consola.prnt("1. Ver mensaje")
				self.consola.prnt("2. Ver confirmaciones del mensaje")
				self.consola.prnt("3. Eliminar mensaje")
				self.consola.prnt("4. Volver al menú anterior")
				opcion = self.consola.askInput("Opcion: ")
				self.consola.clear()
				if opcion == "1":
					self.consola.prnt("===================================")
					self.consola.prnt("Fecha de envío: %s " % self.msj.getFecha().strftime("%d/%m/%Y %H:%M:%S"))
					self.consola.prnt("Campaña: %s" % self.campania)
					self.consola.prnt("Grupo receptor: %s" % self.campania.getGrupoReceptores())
					self.consola.prnt("===================================")
					self.consola.prnt("Mensaje: %s" % self.msj)
					self.consola.prnt("===================================")
					self.consola.askInput("Presione ENTER para volver...")
					self.consola.clear()
					continue
				elif opcion == "2":
					self.consola.prnt("===================================")
					for conf in self.mensaje.getConfirmaciones():
						self.consola.prnt("Receptor: %s" % conf.getReceptor())
						if not conf.huboError():
							self.consola.prnt("Fecha de envío: %s" )
						else:
							self.consola.prnt("ERROR de Envío: %s" % conf.getError())
						self.consola.prnt("===================================")
					self.consola.askInput("Presione ENTER para volver...")
					self.consola.clear()
					continue
				elif opcion == "3":
					self.campania.sacarMensaje(self.msj)
					self.consola.prnt("Mensaje eliminado!")
					self.consola.askInput("Presione ENTER para volver...")
					self.consola.clear()
					break
				elif opcion == "4":
					break
				else:
					self.consola.askInput("Opcion no encontrada!")
					self.consola.askInput("Presione ENTER para volver...")
					self.consola.clear()
					continue
			self.consola.clear()
			self.main.setScreen(ListaMensajes(self.main, self.usuario, self.campania))




