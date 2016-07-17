class UIScreen():
	def __init__(self, unMain):
		self.consola = unMain.consola
		self.main = unMain

	def run(self):
		raise NotImplemented("Screen es abstracta")