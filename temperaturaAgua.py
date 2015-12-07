import os 
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir='/sys/bus/w1/devices/'
device_folder=glob.glob(base_dir+'28*')[0]
device_file= device_folder+'/w1-slave'

#abrir device_file para pasar a archivo
def leertemp_raw():
	t=open(device_file)
	linea=t.readlines()
	t.close()
	return linea
#leer la temperatura desde el sensor
def leertemp():
	linea= leertemp_raw()
	while linea[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		linea= leertemp_raw()
	equals_pos=linea[1].find('t=')
	if equals_pos!= -1:
		temp_string= linea[1][equals_pos+2:]
		#celcius
		temp_c=float(temp_string)/1000.0
		#fahrenheit
		temp_f=temp_c*(9.0/5.0) +32
		return temp_c, temp_f

while True:
	print(leertemp())
	time.sleep(1)
