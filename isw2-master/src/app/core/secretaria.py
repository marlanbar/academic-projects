from .responsable import Responsable
from .supervisor import Supervisor
from .docente import Docente
from .materia import Materia
from .alumno import Alumno
from .turno import Turno
from .curso import Curso

class Secretaria():
	def __init__(self):
		self.relacionAlumnoResponsable = dict()
		self.relacionResponsableAlumno = dict()
		self.responsables = set()
		self.supervisores = set()
		self.docentes = set()
		self.materias = set()
		self.alumnos = set()
		self.cursos = set()
		self.turnos = set()

	def getDocentes(self):
		return set(self.docentes)

	def getSupervisores(self):
		return set(self.supervisores)
		
	def getMaterias(self):
		return set(self.materias)

	def getMateriasPara(self, unaAutoridad, anioCal):
		ret = set()
		for curso in self.cursos:
			if curso.getAnioCal() == anioCal and \
				unaAutoridad.puedeVisualizarInfoDeCurso(curso):
					ret = ret.union(curso.getMaterias())
					
		return ret

	def getTurnos(self):
		return set(self.turnos)

	def getAlumnos(self, unaAutoridad, anioCal):
		ret = set()
		for curso in self.cursos:
			if curso.getAnioCal() == anioCal and \
				unaAutoridad.puedeVisualizarInfoDeCurso(curso):
					ret = ret.union(curso.getAlumnos())
					
		return ret

	def getAlumnosTurno(self, unaAutoridad, unTurno, anioCal):
		ret = set()
		for curso in self.cursos:
			if curso.getAnioCal() == anioCal and \
				curso.getTurno() == unTurno and \
				unaAutoridad.puedeVisualizarInfoDeCurso(curso):
					ret = ret.union(curso.getAlumnos())
					
		return ret

	def getCursos(self, unaAutoridad, anioCal):
		ret = set()
		for curso in self.cursos:
			if curso.getAnioCal() == anioCal and \
				unaAutoridad.puedeVisualizarInfoDeCurso(curso):
					ret.add(curso)
					
		return ret

	def getResponsablesDe(self, unAlumno):
		return self.relacionAlumnoResponsable[unAlumno]

	def getTuteladosPor(self, unResponsable):
		return self.relacionResponsableAlumno[unResponsable]


	def registrarAlumno(self, unAlumno, unConjResponsables):
		if not(unConjResponsables <= self.responsables):
			#Es que nadie piensa en los niños??! D:
			raise Exception('No se pueden registrar Alumnos con Responsables no registrados')

		self.alumnos.add(unAlumno)
		self.relacionAlumnoResponsable[unAlumno] = set(unConjResponsables)

		for responsable in unConjResponsables:
			self.relacionResponsableAlumno[responsable].add(unAlumno)

	def registrarResponsable(self, unResponsable):
		self.responsables.add(unResponsable)
		self.relacionResponsableAlumno[unResponsable] = set()

	def registrarDocente(self, unDocente):
		self.docentes.add(unDocente)

	def registrarSupervisor(self, unSupervisor):
		self.supervisores.add(unSupervisor)

	def registrarMateria(self, unMateria):
		self.materias.add(unMateria)

	def registrarTurno(self, unTurno):
		self.turnos.add(unTurno)

	def registrarCurso(self, unCurso):
		self.cursos.add(unCurso)