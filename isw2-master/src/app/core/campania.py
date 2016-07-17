import datetime

from .aviso import Aviso
from .grupo import Grupo
from .mensaje import Mensaje
from .criterio import Criterio


class Campania():
	#Colaboradores internos:
	#fechaLimite: Datetime
	#nombre: String
	#anioCal: Int

	#Colaboradores externos:
	#mensajes: Conjunto<Mensaje>
	#state: EstadoCampania
	#criterio: Criterio
	#aviso: Aviso
	#grupo: Grupo

	def __init__(self, nombre, anioCal, unAviso, unGrupo, fechaLimite, unCriterio):
		if unAviso.posteriorA(fechaLimite): raise Exception("No se puede crear una Campaña con fecha previa al Aviso")
		self.fechaLimite = fechaLimite
		self.criterio = unCriterio
		self.anioCal = anioCal
		self.nombre = nombre
		self.aviso = unAviso
		self.grupo = unGrupo

		from .campaniaPendiente import CampaniaPendiente
		self.mensajes = set()
		self.state = CampaniaPendiente(self)
	
	def getNombre(self):
		return self.nombre
		
	def getAviso(self):
		return self.aviso
	
	def getAnioCal(self):
		return self.anioCal

	def getFechaLimite(self):
		return self.fechaLimite

	def getGrupoReceptores(self):
		return self.grupo

	def getCriterio(self):
		return self.criterio

	def getMensajes(self):
		return set(self.mensajes)

	def setEstado(self, unEstadoCampania):
		self.state = unEstadoCampania


	def agregarMensaje(self, texto, unTipoMensaje, fecha):
		if self.yaFinalizo(): raise Exception("La campaña ya finalizó y no se le pueden agregar mensajes.")
		if self.antesDe(fecha): raise Exception("El mensaje a agregar no puede estar despues de la fecha de fin de la campaña.")

		msg = Mensaje(texto, unTipoMensaje, fecha, self)
		self.mensajes.add(msg)

	def sacarMensaje(self, mensaje):
		if self.yaFinalizo(): raise Exception("La campaña ya finalizó y no se le pueden sacar mensajes.")
		if not(mensaje.puedeEliminarse()): raise Exception("El mensaje no se puede sacar.")

		assert(mensaje in self.mensajes)
		self.mensajes.remove(mensaje)


	def puedeEliminarse(self):
		if self.yaFinalizo(): return False
		for m in self.mensajes:
			if not(m.puedeEliminarse()): return False
		return True

	def posteriorA(self, fecha):
		return self.fechaLimite > fecha
		
	def antesDe(self, fecha):
		return self.fechaLimite <= fecha

	def cambiarCriterio(self, unCriterio):
		self.criterio = unCriterio

	
	def yaFinalizo(self):
		return self.state.yaFinalizo()

	def yaFueEvaluada(self):
		return self.state.yaFueEvaluada()

	def puedeEvaluarse(self):
		return self.state.puedeEvaluarse()

	def finalizar(self):
		return self.state.finalizar()

	def evaluar(self, unaEvaluacion):
		return self.state.evaluar(unaEvaluacion)

	def getEvaluacion(self):
		return self.state.getEvaluacion()

	def __str__(self):
		return self.nombre
