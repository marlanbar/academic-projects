from .usuario import Usuario

class AdministradorDeSistema():
	#Colaboradores Externos:
	#usuarios: Conjunto<Usuario>

	def __init__(self):
		self.usuarios = set()

	def crearUsuario(self, username, password, unaAutoridad):
  		for i in self.usuarios:
  			if i.getUsername() == username:
  				if i.getAutoridad() == unaAutoridad and \
  					i.validar(username, password):
  						return i
  				else:
  					raise Exception()

  		ret = Usuario(username, password, unaAutoridad)
  		self.usuarios.add(ret)
  		return ret

	def existeUsuario(self, username):
  		for i in self.usuarios:
  			if i.getUsername() == username:
  				return True

  		return False

	def esUsuarioValido(self, username, password):
		for user in self.usuarios:
			if user.validar(username, password):
				return True

		return False
	
	def getUsuarios(self):
		return set(self.usuarios)

	def getUsuario(self, username):
		for user in self.usuarios:
			if user.getUsername() == username:
				return user

		raise Exception("El usuario con 'username'=[%s] no existe." % username)