## Primer TP de Introducción a las Tecnologías del Habla

### Integrantes:

Guillermo Alejandro Gallardo Diez 

Martín Ezequiel Langberg


===

###Instrucciones de Uso

Para utilizar TTS, es necesario ejecutar el archivo tts.py  (ubicado en la carpeta raíz del TP) con dos argumentos:

1. Texto de entrada

2. Ruta del WAV de salida

Ejemplo:

```Bash
python tts.py kakalakapapalapa ./wavs/prueba.wav
```

###Aclaraciones sobre cambios en la entonación

Para cambiar la entonación del WAV y así darle un tono de pregunta, lo que hicimos fue, a través de un script de Praat (ver cambiarPitch.praat) elevar el pitch del sonido a partir de un momento determinado, en función de la cantidad de difonos. 

La fórmula que usamos para modificar el pitch fue asignarle a cada punto `val = f * 1.1` con f el valor ya modificado del punto anterior. De esta manera le dimos una forma de curva creciente que se asemejaba a las pruebas que habiamos hecho previamente en Praat.

Si el pitch supera cierto umbral (que fijamos en 260hz) el valor del punto siguiente pasa a `val = f * 0.3`, empezando a subir nuevamente de la forma anterior. Esta formula así como los valores usados en ellas fueron producto de varias pruebas, en la que se verificaron sus buenos resultados.

###Versión de Praat
Para trabajar utilizamos la versión 5.4 de Praat (Versión Linux). Para evitar problemas de compatibilidad incluimos el compilado dentro de la carpeta.

