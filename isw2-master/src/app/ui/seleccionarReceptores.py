from .consola import Consola
from .uiscreen import UIScreen

from app.core.secretaria import Secretaria
from app.core.materia import Materia
from app.core.curso import Curso
from app.core.turno import Turno

class SeleccionarReceptores(UIScreen):
  def __init__(self, unMain, unUsuario, callbackFn = None):
    super().__init__(unMain)
    self.usuario = unUsuario
    self.callbackFn = callbackFn

    if callbackFn == None:
      def funcion(receptores):
        self.consola.prnt("No se especifico una funcion de Callback. Terminando el programa.")
        self.main.terminate()
      self.callbackFn = funcion


  def run(self):
    self.consola.prnt("Seleccion de receptores")
    cursos = self.main.getSecretaria().getCursos(self.usuario.getAutoridad(), self.main.getReloj().getAnioCal())
    
    #Filtro de cursos por turno
    filtroTurno = self.elegirTurno()
    if filtroTurno is None:
      cursosFiltradosPorTurno = cursos
    else:
      cursosFiltradosPorTurno = [curso for curso in cursos \
                            if curso.getTurno() == filtroTurno]

    #Filtro de cursos por materias
    filtroMateria = self.elegirMateria()
    if filtroMateria is None:
      cursosFiltradosPorTurnoYMateria = cursosFiltradosPorTurno
    else:
      cursosFiltradosPorTurnoYMateria = [curso for curso in cursosFiltradosPorTurno \
                              if filtroMateria in curso.getMaterias()]

    if len(cursosFiltradosPorTurnoYMateria) == 0:
      #No hay cursos con esos filtros
      opcion = ""
      while opcion not in ["s", "n"]:
        self.consola.prnt("No se encontraron cursos con esos filtros.")
        opcion = self.consola.askInput("¿Intentar con otros? S/N").lower()
        self.consola.clear()

      if opcion == "n":
        self.callbackFn(set())

    else:
      curso = self.elegirCurso(cursosFiltradosPorTurnoYMateria)

      alumnos = set()
      if curso is None:
        for curso in cursosFiltradosPorTurnoYMateria:
          alumnos = alumnos.union(curso.getAlumnos())
      else:
        alumnos = curso.getAlumnos()


      #Tipo de receptores
      opciones = ["Solo Alumnos", "Alumnos y sus Padres/Tutores", "Solo Padres/Tutores"]
      tipoReceptor = self.displayConjunto(opciones, "¿Qué tipo de receptores le interesan?", None)

      receptores = set()
      if tipoReceptor == "Solo Alumnos":
        receptores = alumnos
      elif tipoReceptor == "Alumnos y sus Padres/Tutores":
        for a in alumnos:
          receptores.add(a)
          receptores = receptores.union(self.main.getSecretaria().getResponsablesDe(a))
      else:
        for a in alumnos:
          receptores = receptores.union(self.main.getSecretaria().getResponsablesDe(a))

      
      #Filtra receptores
      receptores = list(receptores)
      opcion = -1
      while opcion is not None:
        opcion = self.displayConjunto(receptores, "Indique el número del Receptor para eliminarlo de la lista", "Continuar")
        if opcion is not None:
          receptores.remove(opcion)

      #Llama al callback
      self.callbackFn(receptores)


  def recorrerOpciones(self, lista):
    i = 1
    for l in lista:
      self.consola.prnt("%d. %s" % (i, l))
      i += 1

  def displayConjunto(self, conj, pregunta, noAnswerMsg = "Toda la lista"):
    opcion = -1
    lst = list(conj)
    while opcion not in range(0, len(lst)):
      self.consola.prnt("===========================================================")
      self.consola.prnt(pregunta)
      self.consola.prnt("")

      self.recorrerOpciones(lst)
      if noAnswerMsg is not None: self.consola.prnt("<nada> " +noAnswerMsg)

      self.consola.prnt("")
      self.consola.prnt(pregunta)
      self.consola.prnt("-----------------------------------------------------------")
      self.consola.prnt("")

      opcion = self.consola.askInput("Opcion (Enter para continuar): ")
      self.consola.clear()

      if noAnswerMsg and opcion == "": return None
      try:
        opcion = int(opcion) - 1
      except:
        pass
    return lst[opcion]

  def elegirTurno(self):
    turnos = list(self.main.getSecretaria().getTurnos())
    return self.displayConjunto(turnos, "¿Filtrar por un turno en especial?")

  def elegirMateria(self):
    materias = self.main.getSecretaria().getMateriasPara(self.usuario.getAutoridad(), self.main.getReloj().getAnioCal())
    self.displayConjunto(materias, "¿Filtrar por una materia en especial?")

  def elegirCurso(self, cursos):
    return self.displayConjunto(cursos, "Filtrar por un curso en especial?")


  def elegirAlumnos(self, curso):
    lista_alumnos = []
    terminado = "a"
    while terminado != "s":
      alumnos = displayConjunto(self, curso, "conjunto de alumnos")
      lista_alumnos.append(alumno)
      terminado = self.consola.askInput("¿Finalizar eleccion? S/N")
      terminado.lower()
    self.consola.clear()
    return lista_alumnos
