import Adafruit_DHT as dht
h,t=dht.read_retry(dht.DHT22,8)
list= '{0:0.1f} {1:0.1f}'.format(t,h)
lista=list.split(" ")
print lista
temp= lista[0]
hume=lista[1]
def temperatura(temp):
        temperatura={}
        temperatura["token"]="9H1k2EHf1NNwMZ3uwx2sy7y1lK7jqy71"
        temperatura["id"]=1
        temperatura["value"]=float(temp)
        return temperatura
def humedad(hume):
        humedad={}
        humedad["token"]="9H1k2EHf1NNwMZ3uwx2sy7y1lK7jqy71"
        humedad["id"]=2
        humedad["value"]=float(hume)
        return humedad
def tempdht22():
        t=temperatura(temp)
        return t
def humedht22():
        h=humedad(hume)
        return h
print tempdht22()
print humedht22()
