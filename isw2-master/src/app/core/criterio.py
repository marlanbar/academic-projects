class Criterio():
	#Colaboradores internos:
	#pregunta: String

	def __init__(self, pregunta):
		self.pregunta = pregunta

	def getPregunta(self):
		return self.pregunta

	def __str__(self):
		return self.getPregunta()