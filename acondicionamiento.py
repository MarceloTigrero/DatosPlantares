from locale import normalize
import os
import sys
import numpy as np
import cv2
import serial.tools.list_ports
import serial
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import matplotlib.patches as mpatches
import statsmodels.api as sm


##############################################################################################################################
# la actividad muscular ronda los .1-5mV a una frecuencia de 10kHz   ///http://virtual.cuautitlan.unam.mx/intar/?page_id=977
##############################################################################################################################

Folderbydata = 'Recoleccion1_Conversion'  #2'Recoleccion1_Conversion'
#Folderbydata = 'Recoleccion2'

files = os.listdir( Folderbydata )
#print(files)

datosmaximosenbase = []
datos = []

corte = 5
for file in files:
    data = []
    csv = open(Folderbydata +'/'+file, "r")
    try:
        data = [int(element) for element in csv.read().splitlines()]
    except (ValueError, TypeError):
        #data = []
        for row in open(Folderbydata+'/'+file, "r"):
            #print(row)
            try:
                int(row)
            except (ValueError, TypeError):
                #print('dato'+row)
                #break
                row = 0
            finally:
                row = int(row)
                data.append(row)
    #print(data)
    # pregunto si el archivo tiene datos
    if len(data) > 0:
        data = [data[x] for x in range(0,len(data)) if x >= corte]# cambia el tamaño de la lista cortando los primeros 5 elementos
        if (file.split('.')[0].split('_')[1].startswith('B')):
            datosmaximosenbase.append(max(data))
        else:
            pass
        datos.append(data)
    else:
        print('El archivo '+file+' tiene problemas')

    csv.close()

print(datosmaximosenbase)
prombase = statistics.mean(datosmaximosenbase)
print(prombase)


#normalizacion de los datos
for x in range(0,len(datos)):
    for y in range(0,len(datos[x])):
        if datos[x][y] == 0:
            datos[x][y] = prombase
        datos[x][y] = datos[x][y]/prombase

#de 500 a 495
# deberia tomar samples de muestras de 510 para poder cortar esa parte de la señal

# grafica de los datos
for x in range(0,len(datos)):
    plt.plot(datos[x])
plt.show()



exit()


## alt shift A bloque de codigo comentado






""" 
data = []
csv = open(Folderbydata +'/'+files[0], "r")
    
try:
    data = [int(element) for element in csv.read().splitlines()]
except (ValueError, TypeError):
    for element in csv.read().splitlines():
        try:
            sf = int(element)
        except (ValueError, TypeError):
            sf = 0
        finally:
            data.append(sf)

# eliminacion de datos basura
data = [x for x in data if x != 0]
print(data) 

# normalizacion de datos
data1 = [x/max(data) for x in data]
print(data1)


# mostrar las graficas de la serie de datos

#plt.plot(data)
plt.plot(data1)
plt.show() """







""" 

#normalize('NFKD', datosmaximosenbase).split(' ')
for file in files:
    data = []
    csv = open(Folderbydata +'/'+file, "r")
    try:
        data = [int(element) for element in csv.read().splitlines()]
    except (ValueError, TypeError):
        for element in csv.read().splitlines():
            try:
                sf = int(element)
            except (ValueError, TypeError):
                sf = 0
            finally:
                data.append(sf)
    finally:
        # eliminacion de datos basura
        data = [x for x in data if x != 0]
    if (file.split('.')[0].split('_')[1].startswith('B')):
        pass
    else:
        data = [x/prombase for x in data]
    csv = open(Folderbydata +'/'+file, "w")
    for element in data:
        csv.write(str(element)+'\n')
    csv.close()


# le aplicamos un filtro de movimiento para eliminar ruido y obtener una media de los datos
data_filtered = []
for x in range(0,len(data)):
    if x == 0:
        data_filtered.append(data[x])
    else:
        data_filtered.append(data[x] - data[x-1])

#print(data_filtered)


# le aplicamos un filtro para las señales EMG
data_filtered_emg = []
for x in range(0,len(data_filtered)):
    if x == 0:
        data_filtered_emg.append(data_filtered[x])
    else:
        data_filtered_emg.append(data_filtered[x] - data_filtered[x-1])
#print(data_filtered_emg) 
# #plt.plot(data_filtered)
#plt.plot(data_filtered_emg)"""


