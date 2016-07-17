import datetime

from .consola import Consola
from .uiscreen import UIScreen

from ..core.reloj import Reloj

class AjustarReloj(UIScreen):
	def __init__(self, unMain, unUsuario):
		super().__init__(unMain)
		self.usuario = unUsuario

	def run(self):
		self.consola.prnt("")
		self.consola.prnt("            Ahora: %s" % self.main.getReloj().getFechaYTiempo().strftime("%d/%m/%Y %H:%M:%S"))
		self.consola.prnt("===========================================================")
		self.consola.prnt("1. Ajustar fecha")
		self.consola.prnt("2. Ajustar tiempo")
		self.consola.prnt("3. Avanzar una cantidad de dias")
		self.consola.prnt("4. Correr procesos dependientes del tiempo")
		self.consola.prnt("-----------------------------------------------------------")
		self.consola.prnt("9. Volver a la pantalla anterior")
		self.consola.prnt("")
		
		opt = self.consola.askInput("Ingrese el número de la opcion que le interesa: ")
		if opt == "1":
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")
			inputDate = self.consola.askInput("Ingrese la fecha en formato DD/MM/YYYY: ")
			try:
				date = datetime.datetime.strptime(inputDate, "%d/%m/%Y")

				self.consola.clear()
				self.main.getReloj().resetFechaYTiempo(datetime.datetime.combine(date, self.main.getReloj().getTiempo()))
			except:
				self.consola.clear()
				self.consola.prnt("[ERROR] La fecha ingresada es inválida")
		elif opt == "2":
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")
			inputTime = self.consola.askInput("Ingrese el tiempo en formato HH:MM:SS: ")
			try:
				time = datetime.datetime.strptime(inputTime, "%H:%M:%S")

				self.consola.clear()
				self.main.getReloj().resetFechaYTiempo(datetime.datetime.combine(self.main.getReloj().getFecha(), time.time()))
			except:
				self.consola.clear()
				self.consola.prnt("[ERROR] El tiempo ingresado es inválido")
		elif opt == "3":
			self.consola.prnt("-----------------------------------------------------------")
			self.consola.prnt("")
			inputDays = self.consola.askInput("Ingrese la cantidad de dias: ")
			try:
				days = datetime.timedelta(days=int(inputDays))
			except:
				days = None
				self.consola.clear()
				self.consola.prnt("[ERROR] La cantidad ingresada es inválida")

			if days is not None:
				self.consola.clear()
				self.main.getReloj().resetFechaYTiempo(self.main.getReloj().getFechaYTiempo() + days)
		elif opt == "4":
			self.consola.clear()
			self.main.getReloj().notificar()
			self.consola.prnt("[MSG] Procesos ejecutados")
		elif opt == "9":
			from .homeScreen import HomeScreen
			self.consola.clear()
			self.main.setScreen(HomeScreen(self.main, self.usuario))
		else:
			self.consola.clear()
