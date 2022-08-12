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



Folderbydata = 'Recoleccion1_Conversion' 

""" El archivo S101_B_M2.csv no tiene datos
El archivo S101_B_M21.csv no tiene datos
El archivo S101_B_M28.csv no tiene datos
El archivo S101_B_M42.csv no tiene datos
El archivo S101_B_M63.csv no tiene datos
El archivo S101_RDH_M31.csv no tiene datos
El archivo S101_RDL_M2.csv no tiene datos
El archivo S101_RDL_M6.csv no tiene datos
El archivo S101_RDL_M61.csv no tiene datos
El archivo S101_RDL_M78.csv no tiene datos
El archivo S101_RDL_M90.csv no tiene datos
El archivo S101_RDN_M0.csv no tiene datos
El archivo S101_RDN_M2.csv no tiene datos
El archivo S101_RDN_M21.csv no tiene datos
El archivo S101_RDN_M28.csv no tiene datos
El archivo S101_RDN_M3.csv no tiene datos
El archivo S101_RDN_M43.csv no tiene datos
El archivo S101_RDN_M5.csv no tiene datos
El archivo S101_RDN_M81.csv no tiene datos
El archivo S101_RUH_M20.csv no tiene datos
El archivo S101_RUH_M38.csv no tiene datos
El archivo S101_RUH_M47.csv no tiene datos
El archivo S101_RUH_M77.csv no tiene datos
El archivo S101_RUL_M12.csv no tiene datos
El archivo S101_RUL_M23.csv no tiene datos
El archivo S101_RUN_M12.csv no tiene datos
El archivo S101_RUN_M20.csv no tiene datos
El archivo S101_RUN_M42.csv no tiene datos
El archivo S101_RUN_M43.csv no tiene datos
El archivo S101_RUN_M6.csv no tiene datos
El archivo S101_RUN_M8.csv no tiene datos """


# read data S101_B_M2.csv

file_data = open(Folderbydata+'/S101_B_M2.csv', "r")
#print(file_data)
data = []
for row in open(Folderbydata+'/S101_B_M2.csv', "r"):
    print(row)
    try:
        int(row)
    except (ValueError, TypeError):
        print('dato'+row)
        #break
        row = 0
    finally:
        row = int(row)
        data.append(row)
print(data)
print(len(data))
        


"""
data = []
csv = open(Folderbydata +'/S101_B_M2.csv', "r")#2 
print(csv)
# llena la lista con los datos del archivo
#
#data = [int(element) for element in csv.read().splitlines()]

try:
    data = [int(element) for element in csv.read().splitlines()]
    print('try')
except (ValueError, TypeError):
    # muestra el error 
    # decodifica los datos del archivo

    print(csv.read().splitlines())

    #for element in csv.read().splitlines():
    for element in csv:
        try:
            print('try2:' + element)
            element = int(element)
        except (ValueError, TypeError):
            print('except2:' +element)
            element = 0
        else:
            data.append(element)
    print('except')
print(data)
print(len(data))
exit()
#cvs.read().splitlines() """
""" try:
    data = [int(element) for element in csv.read().splitlines()]
except (ValueError, TypeError):
    for element in csv.read().splitlines():
        try:
            sf = int(element)
        except (ValueError, TypeError):
            sf = 0
            data.append(sf)
        else:
            data.append(sf)
#print(data) """




# 


# #print(files)