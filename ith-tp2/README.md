## Segundo TP de Introducción a las Tecnologías del Habla

### Integrantes:

Guillermo Alejandro Gallardo Diez 
Martín Ezequiel Langberg

===

###Instrucciones de Uso

Para utilizar el clasificador, es necesario ejecutar el archivo genero.py con las variables de las rutas de OpenSmile y Weka seteadas, con la ruta del archivo a procesar como argumento.

Ejemplos:

#### Variables

```Python
rutaOpensmile = "~/workspace/ith-tp2/opensmile" 
rutaWeka = "/usr/share/java/weka.jar"
```
#### Ruta del WAV a procesar

```Bash
python genero.py /path/to/input.wav
```
###Versión de las aplicaciones utilizadas
Para trabajar utilizamos:

* La versión svn_trunk de OpenSmile (Versión Linux 64 bits)
   Build date: Oct  8 2014 (Wed Oct  8 11:24:29 ART 2014)
* La versión 3.6.10 de Weka

### Selección de atributos y elección del modelo

Para la selección de los atributos probamos 3 métodos/evaluadores: Greedy, Genetic (junto con J48) y Ranker (InfoGain). A partir de los mejores 400 atributos de Ranker, decidimos hacer un refinamiento de los 40 mejores eligiendolos a partir del puntaje que tenían en los otros dos métodos, al que llamamos método "heurístico". Finalmente esta selección resultó ser mucho más efectiva que la selección Ranker.

La lista de atributos "heurística" es la siguiente (ver ```output_heu.arff```):

```
60, 17, 140, 597, 663, 1431, 1440, 63, 270, 639, 683, 684, 1441, 42, 255, 257, 278, 675, 1329, 1390, 62, 244, 276, 528, 656, 685, 1433, 1445, 234, 269, 290, 326, 654, 662, 690, 1439, 6, 9, 57, 1583
```
El atributo 1583 hace referencia al género del hablante.
Para la elección del modelo pusimos a prueba a los distintos clasificadores con una gran variedad de algoritmos de aprendizaje ofrecidos por Weka, que permitía evaluarlos rápidamente con el modo de 5-fold Cross Validation, arrojando el porcentaje de aciertos. Finalmente decidimos usar el algoritmo `functions.SMO` que arrojó un porcentaje del 98.9% de aciertos, por sobre los demás, que se encontraron entre el 93% y el 95%.

### Resultados Obtenidos

#### Selección Heurística - functions.SMO 

```
=== Summary === 
Correctly Classified Instances         178               98.8889 %
Incorrectly Classified Instances         2                1.1111 %
Kappa statistic                          0.9778
Mean absolute error                      0.0111
Root mean squared error                  0.1054
Relative absolute error                  2.2222 %
Root relative squared error             21.0819 %
Total Number of Instances              180     
```

