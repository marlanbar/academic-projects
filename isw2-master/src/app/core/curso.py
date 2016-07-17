import datetime

from .turno import Turno
from .materia import Materia
from .docente import Docente


class Curso():
	#Colaboradores Internos:
	#alumnos: Conjunto<Alumno>
	#nombre: String
	#anioCal: Int

	#Colaboradores externos:
	#docente: Docente
	#turno: Turno
	#materias: Conjunto<Materia>
	
	def __init__(self, nombre, anioCal, unDocente, turno, conjMaterias):
		self.materias = set(conjMaterias)
		self.docente = unDocente
		self.anioCal = anioCal
		self.nombre = nombre
		self.alumnos = set()
		self.turno = turno

	def getNombre(self):
		return self.nombre

	def getAnioCal(self):
		return self.anioCal

	def getDocente(self):
		return self.docente

	def getMaterias(self):
		return set(self.materias)

	def getTurno(self):
		return self.turno

	def getAlumnos(self):
		return set(self.alumnos)

	def agregarAlumno(self, unAlumno):
		self.alumnos.add(unAlumno)

	def sacarAlumno(self, unAlumno):
		assert(unAlumno in self.alumnos)
		self.alumnos.remove(unAlumno)

	def __str__(self):
		return "%s [%s]" % (self.getNombre(), self.getAnioCal())