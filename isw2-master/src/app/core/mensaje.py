import datetime


class Mensaje(object):
  #Colaboradores Internos
  #texto: String
  #fecha: Datetime
  
  #Colaboradores Externos
  #tipoMensaje: TipoMensaje
  #state: EstadoMensaje
  #campania: Campania


  def __init__(self, texto, unTipoMensaje, fecha, unaCampania):
    self.texto = texto
    self.fecha = fecha
    self.campania = unaCampania
    self.tipoMensaje = unTipoMensaje

    from .mensajeProgramado import MensajeProgramado
    self.state = MensajeProgramado(self)

  def getTexto(self):
    return self.texto

  def getTipoMensaje(self):
    return self.tipoMensaje

  def getFecha(self):
    return self.fecha

  def getCampania(self):
    return self.campania

  
  def setEstado(self, unEstadoMensaje):
    self.state = unEstadoMensaje

  def puedeEliminarse(self):
    return self.estaPendiente() and (len(self.getConfirmaciones()) == 0)

  def estaPendiente(self):
    return self.state.estaPendiente()

  def enviarSiPendiente(self, unMensajero):
    self.state.enviarSiPendiente(unMensajero)

  def getConfirmaciones(self):
    return self.state.getConfirmaciones()


  def posteriorA(self, fecha):
    return self.fecha > fecha 

  def antesDe(self, fecha):
    return self.fecha <= fecha
  
  def __str__(self):
    return self.texto