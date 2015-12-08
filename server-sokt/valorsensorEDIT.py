#leer datos de cualquier sensor , que retorne True or False or valor
import os 
import glob

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

#base_dir='/sys/bus/w1/devices/'
#device_folder=glob.glob(base_dir+'28*')[0]
#device_file= device_folder+'/w1-slave'

def leervalor():
	t=open(device_file) #archivo con valores de los sensores
	linea=t.readlines()
	t.close()
	return linea

def valores():
	linea= leervalor()
	linea= linea.strip()
	for x in linea:
		
