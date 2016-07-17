import datetime

from app.ui.login import Login
from app.ui.consola import Consola
from app.ui.homeScreen import HomeScreen
from app.ui.uicampania import UICampania

from app.core.reloj import Reloj
from app.core.mensajeria import Mensajeria
from app.core.secretaria import Secretaria
from app.core.administradorDeSistema import AdministradorDeSistema

from app.core.finalizadorDeCampanias import FinalizadorDeCampanias

from app.core.mensajeroDemo import MensajeroDemo
from app.core.responsable import Responsable
from app.core.tipoMensaje import TipoMensaje
from app.core.supervisor import Supervisor
from app.core.docente import Docente
from app.core.materia import Materia
from app.core.alumno import Alumno
from app.core.turno import Turno
from app.core.curso import Curso

from app.core.criterio import Criterio
#from app.core.mensaje import Mensaje

class Main():
	#Colaboradores externos
	#admin: AdministradorDeSistema
	#mensajero: MensajeroDemo
	#mensajeria: Mensajeria
	#secretaria: Secretaria
	#consola: Consola
	#screen: Screen
	#reloj: Reloj
	

	#Colaboradores internos
	#loop: Bool

	def __init__(self):
		self.loop = True
		self.consola = Consola()
		self.screen = Login(self)

		self.reloj = Reloj(datetime.datetime.now())
		self.secretaria = Secretaria()
		self.admin = AdministradorDeSistema()

		
		self.mensajero = MensajeroDemo(self.reloj)
		self.mensajeria = Mensajeria(self.admin, self.mensajero, self.reloj)
		finalizador = FinalizadorDeCampanias(self.admin, self.reloj)

		self.reloj.agregarNotificador(self.mensajeria)
		self.reloj.agregarNotificador(finalizador)

		self.loadSomeEntities()

	def loadSomeEntities(self):
		#Creo un docente
		doc = Docente("Severus Snape")
		self.secretaria.registrarDocente(doc)

		#Creo el user
		user = self.admin.crearUsuario("severus", "lily<3", doc)

		#Agrego Turnos
		turnos = [Turno("Mañana"), Turno("Tarde"), Turno("Doble")]
		for t in turnos:
			self.secretaria.registrarTurno(t)

		#Agrego Materias
		materias = [Materia("Herbologia"), Materia("Transfiguracion"), Materia("Defensa contra las Artes Oscuras")]
		for m in materias:
			self.secretaria.registrarMateria(m)

		#Agrego Responsables
		responsables = [Responsable("Lucious Malfoy", "1234-5678", "8.457.215"),
			Responsable("Narcissa Malfoy", "3634-6678", "8.573.214"),
			Responsable("Sirius Black", "824-5668", "18.456.456")]
		for r in responsables:
			self.secretaria.registrarResponsable(r)

		#Agrego Alumnos
		alumnos = [Alumno("Harry Potter", "5555-5555", "25.215.498", datetime.date(1980, 7, 31)),
			Alumno("Draco Malfoy", "1548-8487", "25.200.234", datetime.date(1980, 6, 5))
		]
		self.secretaria.registrarAlumno(alumnos[0], {responsables[2]})
		self.secretaria.registrarAlumno(alumnos[1], set(responsables[0:1]))

		#Agrego Cursos
		curso = Curso("Gryffindor", self.reloj.getAnioCal(), doc, turnos[2], materias)
		self.secretaria.registrarCurso(curso)
		for a in alumnos:
			curso.agregarAlumno(a)


		#Agrego Tipos de Mensaje
		tipoMensajes = [TipoMensaje("Anuncio"), TipoMensaje("Recordatorio"), TipoMensaje("Asignacion"), TipoMensaje("Aliento")]
		for t in tipoMensajes:
			self.mensajeria.registrarTipoMensaje(t)


		#Agrego Avisos
		a1 = user.crearAviso("Mantenerse lejos del Bosque Prohibido", self.reloj.getFecha() + datetime.timedelta(days=31))
		user.crearAviso("Examen de DADA", self.reloj.getFecha() + datetime.timedelta(days=14))


		camp = user.crearCampania("Campaña Test", self.reloj.getAnioCal(), a1, \
			user.crearGrupo("Grupo Campaña Test", self.reloj.getAnioCal()), \
			a1.getFecha(), Criterio("Pensa un numero entero del 0 al 100"))

		camp.getGrupoReceptores().agregar(alumnos[0])


		self.consola.clear()
		self.screen = HomeScreen(self, user)


	def setScreen(self, screen):
		self.screen = screen
		
	def terminate(self):
		self.loop = False

	def start(self):
		while (self.loop):
			self.screen.run()


	def getAdministrador(self):
		return self.admin
	def getSecretaria(self):
		return self.secretaria
	def getMensajeroDemo(self):
		return self.mensajero
	def getMensajeria(self):
		return self.mensajeria
	def getReloj(self):
		return self.reloj

if __name__ == "__main__":
	m = Main()
	m.start()