entrada = "./tmp.arff"
salida = "./tmp.arff"
data  = []

#Saco los atributos del primer archivo
with open(entrada, 'r') as at_file:
    atributos = at_file.readlines()
    
    atributos[2] = ''
    #linea 1586 es @attribute numeric_class numeric     
    atributos[1585] = "@attribute gender {m,f}\n"

    #ultima linea es data  
    data.extend(atributos[:-1])
        
#ultima linea comienza con 'noname' y termina ,0.0
data.append(atributos[-1][9:-4] + "?" + "\n")

   
with open(salida,'w') as current:
        current.writelines(data)       