from .campania import Campania
from .aviso import Aviso
from .grupo import Grupo

class Usuario():
	#Colaboradores Internos:
	#username: String
	#password: String

	#Colaboradores externos:
	#campanias: Conjunto<Campania>
	#grupos: Conjunto<Grupos>
	#avisos: Conjunto<Aviso>
	#autoridad: Autoridad

	def __init__(self, username, password, unaAutoridad):
		self.autoridad = unaAutoridad
		self.username = username
		self.password = password

		self.campanias = set()
		self.grupos = set()
		self.avisos = set()

	def getUsername(self):
		return self.username

	def getAutoridad(self):
		return self.autoridad

	def getAvisos(self):
		return set(self.avisos)

	def getGrupos(self):
		return set(self.grupos)

	def getCampanias(self):
		return set(self.campanias)

	def validar(self, username, password):
		return username == self.username and self.password == password

	def cambiarPassword(self, password):
		self.password = password


	def crearAviso(self, texto, fecha):
		for i in self.avisos:
			if i.getTexto() == texto and \
				i.getFecha() == fecha:
					return i

		ret = Aviso(texto, fecha)
		self.avisos.add(ret)
		return ret

	def crearGrupo(self, nombre, anioCal):
		for i in self.grupos:
			if i.getNombre() == nombre and \
				i.getAnioCal() == anioCal:
					return i

		ret = Grupo(nombre, anioCal)
		self.grupos.add(ret)
		return ret

	def crearCampania(self, nombre, anioCal, unAviso, unGrupo, fechaLimite, unCriterio):
		for i in self.campanias:
			if i.getNombre() == nombre and \
				i.getAnioCal() == anioCal and \
				i.getAviso() == unAviso and \
				i.getGrupo() == unGrupo and \
				i.getFechaLimite() == fechaLimite and \
				i.getCriterio() == unCriterio:
					return i

		if not(unAviso in self.avisos):
			raise Exception("El aviso no es del usuario")
		if not(unGrupo in self.grupos):
			raise Exception("El grupo no es del usuario")

		ret = Campania(nombre, anioCal, unAviso, unGrupo, fechaLimite, unCriterio)
		self.campanias.add(ret)
		return ret

	def eliminarAviso(self, unAviso):
		assert(unAviso in self.avisos)

		for c in self.campanias:
			if c.getAviso() == unAviso: raise Exception("No se puede eliminar el aviso porque pertenece a una Campaña.")
		self.avisos.remove(unAviso)

	def eliminarGrupo(self, unGrupo):
		assert(unGrupo in self.grupos)

		for c in self.campanias:
			if c.getGrupoReceptores() == unGrupo: raise Exception("No se puede eliminar el grupo porque pertenece a una Campaña.")
		self.grupos.remove(unGrupo)

	def eliminarCampania(self, unaCampania):
		assert(unaCampania in self.campanias)
		self.campanias.remove(unaCampania)

	def __str__(self):
		return self.username	