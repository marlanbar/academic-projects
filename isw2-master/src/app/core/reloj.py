import datetime


class Reloj():
	#Colaboradores Internos:
	#tiempoSeteado: DateTime
	#momentoCuandoSeteo: DateTime
	#notificadores: Conjunto<Notificador>

	def __init__(self, unaFechaYTiempo):
		self.notificadores = set()
		self.resetFechaYTiempo(unaFechaYTiempo)

	def agregarNotificador(self, unNotificador):
		self.notificadores.add(unNotificador)

	def sacarNotificador(self, unNotificador):
		self.notificadores.remove(unNotificador)

	def notificar(self):
		for notif in self.notificadores:
			notif.serNotificado()


	def getAnioCal(self):
		return self.getFechaYTiempo().year

	def getFecha(self):
		return self.getFechaYTiempo().date()

	def getTiempo(self):
		return self.getFechaYTiempo().time()

	def getFechaYTiempo(self):
		return self.tiempoSeteado + (datetime.datetime.now() - self.momentoCuandoSeteo)

	def resetFechaYTiempo(self, unaFechaYTiempo):
		self.momentoCuandoSeteo = datetime.datetime.now()
		self.tiempoSeteado = unaFechaYTiempo
		self.notificar()