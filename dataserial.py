#ctrl k c para comentar
#ctrl k u para descomentar
#ctrl k d para duplicar
#ctrl k b para borrar
#ctrl k a para abrir
#ctrl k s para guardar
#ctrl k o para abrir en otra ventana
#ctrl k p para guardar en otra ventana
#ctrl k f para buscar
#ctrl k r para reemplazar
#ctrl k z para deshacer
#ctrl k y para rehacer

# from numpy import var
# import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()
# serialInst = serial.Serial()

# portList=[]

# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))

# val = input("select port COM:")

# for x in range(0,len(portList)):
#     if portList[x].startswith("COM"+str(val)):
#         portVar = "COM"+str(val)
#         print(portList[x])
    
# serialInst.baudrate = 115200
# serialInst.port = portVar
# serialInst.open() 

# while True:
#     if serialInst.in_waiting:
#         #serialInst.write("hello word")
#         packet = serialInst.readline()
#         print(packet.strip().decode('utf-8'))
#         #print(packet.decode())
#         #print(packet.decode('utf'))


import numpy as np
import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random
from numpy import var
import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

import serial.tools.list_ports
#
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
#
portList=[]
#
Data = []
n_b=0
n_d_h,n_d_n,n_d_l=0,0,0
n_u_h,n_u_n,n_u_l=0,0,0
valores=0
#
#   streams = resolve_stream()



def base():# descanso()
    img = cv2.imread('Imagen_jpg/B.jpg')# direccion de la imagen
    cv2.namedWindow('FOCUS-ON', cv2.WINDOW_NORMAL)# nombre de la ventana
    # cv2.resizeWindow('FOCUS-ON', 600,600)# tamaño de la ventana
    # cv2.imshow('FOCUS-ON',img)# muestra la imagen\
    cv2.imshow('FOCUS-ON',img)# muestra la imagen
    cv2.waitKey(0)# espera a que se presione una tecla

    # cv2.setWindowProperty('FOCUS-ON', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)# ventana en pantalla completa
    # cv2.imshow('Image', img)# muestra la imagen  en la ventana de nombre "Image"
    # cv2.waitKey(250)# tiempo de espera
# funcion que muestra la imagen de descanso en pantalla secundaria
def descanso():
    img = cv2.imread('Imagen_jpg/RB.jpg')# direccion de la imagen
    cv2.namedWindow('FOCUS-ON', cv2.WINDOW_NORMAL)# nombre de la ventana
    # le asigna el tamaño de la ventana
    cv2.resizeWindow('FOCUS-ON', 600,600)# tamaño de la ventana
    # la ubicamos en la pantalla completa y la muestra en pantalla secundaria
    #cv2.setWindowProperty('FOCUS-ON', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)# ventana en pantalla completa
    cv2.imshow('FOCUS-ON', img)# muestra la imagen  en la ventana de nombre "Image"
    cv2.waitKey(250)# tiempo de espera


print("looking for an EMG stream...")
opciones = ["Base","Down High","Down Normal","Down Low","Up High","Up Normal","Up Low"]

while __name__ == '__main__':
    #print(":eyes:")
    base()    
    #preguntamos si la pantalla esta activa y abierta
    
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     print("saliendo")
    #     break
    pass2 = input('Todos listos (K):').upper()
    while pass2 != 'K':
        pass 

    #esperamos hasta que se habilite la pantalla
    while cv2.getWindowProperty('FOCUS-ON',cv2.WND_PROP_VISIBLE) < 1:
        print("waiting for screen")
        pass
    
    #esperamos hasta que se cierre la pantalla
    while cv2.getWindowProperty('FOCUS-ON',cv2.WND_PROP_VISIBLE) > 0:
        print("waiting for screen to close")
        pass

    

    


