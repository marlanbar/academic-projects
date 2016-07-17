#! bin/env/python


import sys
import os

rutaOpensmile = "~/workspace/ith-tp2/opensmile" 
rutaWeka = "/usr/share/java/weka.jar"
def main():
	if len(sys.argv) != 2:
		print "Modo de Uso: ./genero.py rutaArchivo "
		return
	filename = sys.argv[1]
	os.system("{}/SMILExtract -C {}/config/IS10_paraling.conf -I {} -O tmp.arff 2> /dev/null 1> /dev/null".format(rutaOpensmile, rutaOpensmile, filename))
	os.system("python test2data.py")
	os.system("java -cp {} weka.filters.unsupervised.attribute.Remove -V -R \"60, 17, 140, 597, 663, 1431, 1440, 63, 270, 639, 683, 684, 1441, 42, 255, 257, 278, 675, 1329, 1390, 62, 244, 276, 528, 656, 685, 1433, 1445, 234, 269, 290, 326, 654, 662, 690, 1439, 6, 9, 57, 1583\" -i tmp.arff -o tmp2.arff".format(rutaWeka))
	os.system("rm tmp.arff")
	os.system("rm smile.log")
	os.system("java -cp {} weka.classifiers.functions.SMO -l ./model/SMO_Heu.model -T tmp2.arff -p 0".format(rutaWeka)+"| grep -e \"[mf]\" | awk '{ print substr($3,3,3) }'")
	os.system("rm tmp2.arff")



if __name__ == '__main__':
	main()


# [60, 17, 140, 597, 663, 1431, 1440, 63, 270, 639, 683, 684, 1441, 42, 255, 257, 278, 675, 1329, 1390, 62, 244, 276, 528, 656, 685, 1433, 1445, 234, 269, 290, 326, 654, 662, 690, 1439, 6, 9, 57, 1583]