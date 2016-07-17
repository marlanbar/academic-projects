from os import walk

sujetos = "./arffs/"
nprueba = 10
salida = "./data/data.arff"

files = []
data  = []

for (dirpath, dirnames, filenames) in walk(sujetos):
    files.extend(filenames)
    break

files.sort()

#Saco los atributos del primer archivo
with open(sujetos+files[0], 'r') as at_file:
    atributos = at_file.readlines()
    
    atributos[2] = ''
    #linea 1586 es @attribute numeric_class numeric     
    atributos[1585] = "@attribute gender {m,f}\n"
    
    #ultima linea es data
    atributos = atributos[:-1]

    data.extend(atributos)
        
for arf in files:
    with open(sujetos+arf,'r') as current:
        texto = current.readlines()
    
    genero = arf[4]
    
    #ultima linea comienza con 'noname' y termina ,0.0
    data.append(texto[-1][9:-4] + genero + "\n")

   
with open(salida,'w') as current:
        current.writelines(data)
       
