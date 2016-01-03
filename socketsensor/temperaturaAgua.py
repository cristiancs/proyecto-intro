import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir='/sys/bus/w1/devices/'
device_folder=glob.glob(base_dir+'28*')[0]
device_file= device_folder+'/w1_slave'

#abrir device_file para pasar a archivo
def read_temp_raw():
        f=open(device_file,"r")
        lines=f.readlines()
        f.close()
        return lines
#leer la temperatura desde el sensor
def read_temp():
        lines= read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines= read_temp_raw()
        equals_pos=lines[1].find('t=')
        if equals_pos!= -1:
                temp_string= lines[1][equals_pos+2:]
                #celcius
                temp_c=float(temp_string)/1000.0
                return temp_c

def readDatos():
        dic={}
        datos=read_temp()
        dic["value"]=datos
        dic["id"]=3
        dic["token"]="9H1k2EHf1NNwMZ3uwx2sy7y1lK7jqy71"
        return dic
