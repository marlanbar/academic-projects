''' 
Objeto que permite crear el script de praat
'''

class Scripter():
        
    def __init__(self, difonosFolder):
        self._script = ""
        self._cantidad = 1
        self._difFold  = difonosFolder
            
    def agregarDifono(self, difono):
        difFold = self._difFold
        script  = self._script
        
        script += 'Read from file: "{}/{}.wav"\n'.format(difFold,difono)
        script += 'selectObject: "Sound {}"\n'.format(difono)
        script += 'Rename: "difono{}"\n'.format(self._cantidad)
        
        self._cantidad +=1
        self._script = script
    
    def concatenar(self, salida):
        if self._cantidad == 1:
            return
                
        script = self._script
        script += 'selectObject:"Sound difono1"\n' 
        
        for i in xrange(2,self._cantidad):
            script += 'plusObject:"Sound difono{}"\n'.format(str(i))
            
        script += 'Concatenate recoverably\n'
        script += 'selectObject: "Sound chain"\n'
        script += 'Save as WAV file: "{}"\n'.format(salida)
        
        self._script = script
        
    def escribirScript(self, archivo):
        f = open(archivo,'w')
        f.write(self._script)
        f.close()
        
