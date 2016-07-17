import getpass

class Consola:
	def prnt(self, *args):
		print(*args)
	
	def askInput(self, text):
		entrada = input(text)
		return entrada

	def askShadowInput(self, text):
		return getpass.getpass(text)

	def clear(self):
		for i in range(1, 40):
			self.prnt("")
