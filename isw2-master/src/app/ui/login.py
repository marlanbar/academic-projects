from .consola import Consola
from .uiscreen import UIScreen
from .homeScreen import HomeScreen

from ..core.usuario import Usuario
from ..core.docente import Docente

class Login(UIScreen):
	def __init__(self, unMain):
		super().__init__(unMain)

	def run(self):
		self.consola.prnt("================")
		self.consola.prnt("Inicio de sesion")
		self.consola.prnt("")
		user = self.consola.askInput("Usuario: ")
		passwd = self.consola.askShadowInput("Password: ")

		if self.main.getAdministrador().esUsuarioValido(user, passwd):
			user = self.main.admin.getUsuario(user)

			self.consola.clear()
			self.main.setScreen(HomeScreen(self.main, user))
		else:
			self.consola.clear()
			self.consola.prnt("[Error] Usuario y contraseña incorrectos.")
