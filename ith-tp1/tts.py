#!/usr/bin/python

#! /usr/bin/python
''' 
Entrada: S:string F:file
Salida:  S sintetizado en F
'''
import sys
import os
import re
from src.scripter import Scripter


consonantes = ["l","s","p","k","m"]
vocales = ["a","A"]
difonosFolder = "difonos"

def valido(texto):
    ''' Dado un input determina si el mismo es valido
        Un input valido es de la forma: c(vc)*v | v(cv)* '''

    if texto[-1] == "?":
        texto = texto[:-1]

    largo = len(texto)
    inicio = 1 if texto[0] in vocales else 0

    inicioConVoc = texto[0] in consonantes + vocales
    largoPar = (largo - inicio) % 2 == 0

    valido = inicioConVoc and largoPar
    
    for i in xrange(inicio,largo,2):
        convoc = (texto[i] in consonantes) and (texto[i+1] in vocales)
        valido = valido and convoc
  
    return valido


def textoADifonos(texto):
    ''' Dado un texto valido lo descompone en difonos '''

    difonos = []
    
    esPregunta = texto[-1] == "?"
    if esPregunta:
        texto = texto[:-1] 
    
    difonos.append("-"+texto[0])
     
    for i in xrange(len(texto)-1):
        difonos.append(texto[i]+texto[i+1])
        
    difonos.append(texto[-1]+"-")

    return difonos


def procesarAudio(difonos,salida):
    
    miScripter = Scripter(difonosFolder)

    for dif in difonos:
        miScripter.agregarDifono(dif)
    
    miScripter.concatenar(salida)
    
    miScripter.escribirScript("tmp.script.praat")

    os.system('./praat tmp.script.praat')
    os.system('rm tmp.script.praat')

def procesarPregunta(cantDifonos, salida):
    os.system('./praat cambiarPitch.praat {0} {1}'.format(cantDifonos, salida))


# ---------------------------------------------------------------    

def main():
    params = sys.argv

    if len(params) != 3:
        print " TTS | Gallardo - Langberg "
        print " Modo de uso: tts.py string file "
        return
             
    _, texto, salida = params

    if not valido(texto):
        print " String ingresado NO VALIDO"
        return

    
    difonos = textoADifonos(texto)
    cantDifonos = len(difonos)
    
    procesarAudio(difonos,salida)

    esPregunta = texto[-1] == "?"
    if esPregunta:
        procesarPregunta(cantDifonos, salida)

if __name__ == "__main__":
    main()
