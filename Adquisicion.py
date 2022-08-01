## Prospecto de Tesis  Senales EMG Para Protesis o Ortesis Plantar


import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random

Data = []
n_b=0
n_d_h,n_d_n,n_d_l=0,0,0
n_u_h,n_u_n,n_u_l=0,0,0
valores=0
#streams = resolve_stream('type', 'EEG')
#print(":eyes:")
#1streams = resolve_stream('type', 'EEG')
streams = resolve_stream()
#print(":eyes:")
#inlet = StreamInlet(streams[0])
#print(":eyes:")
def base():# descanso()
    img = cv2.imread('Imagenes/Base.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', img)
    cv2.waitKey(250)

def data(N,Tipo,Tipo2,Tipo3,Tipo4):# N (#), Tipo (R/L), Tipo2 (U/D), Tipo3 (H/N/L), Tipo4 (#) SNRUH_R1M1
    name = "S"+str(N)+str(Tipo)+str(Tipo2)+str(Tipo3)+"_R"+str(Run)+"M"+str(Tipo4)
    imagen='Imagen_jpg/'+str(Tipo)+str(Tipo2)+str(Tipo3)+'.jpg'
    print(imagen)
    im = cv2.imread(imagen)
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        Data.append(sample)
        if len(Data) == 500:# Numero de datos a 100Hz
            cv2.waitKey(1)
            df = pd.DataFrame(Data)
            df.to_csv("Recoleccion/"+name+'.csv')
            Data.clear()
            break


N = input('Ingresar identificación del sujeto: ') # Subject
muestras = int(input('Ingresar numero de muestras : ')) # Muestras
Tipo = input('Ingresar el tipo de experimento a realizar (L/R): ')   # Tipos posibles L , R
Run = int(input('Ingresar el número de series: ')) # 1 por defout
print("looking for an EMG stream...")
opciones = ["Base","Down High","Down Normal","Down Low","Up High","Up Normal","Up Low"]

while __name__ == '__main__':
    #print(":eyes:")
    base()
    while valores != (6*muestras):# Numero de variables * Numero de muestras
        valores = n_b+n_d_h+n_d_n+n_d_l+n_u_h+n_u_n+n_u_l
        print(valores)
        print(muestras)
        opcion = random.randint(0, 6)
        print("aleatorio :"+ str(opcion) +" "+opciones[opcion])
        if opcion == 0 and n_b != muestras:
            data(N,Tipo,'','',n_b)#Tipo2 (U/D), Tipo3 (H/N/L),
            base()
            n_b += 1
        elif opcion == 1 and n_d_h != muestras:
            data(N,Tipo,'D','H',n_d_h)
            base()
            n_d_h += 1
        elif opcion == 2 and n_d_n != muestras:
            data(N,Tipo,'D','N',n_d_n)
            base()
            n_d_n += 1
        elif opcion == 3 and n_d_l != muestras:
            data(N,Tipo,'D','L',n_d_l)
            base()
            n_d_l += 1
        elif opcion == 4 and n_u_h != muestras:
            data(N,Tipo,'U','H',n_u_h)
            base()
            n_u_h += 1
        elif opcion == 5 and n_u_n != muestras:
            data(N,Tipo,'U','N',n_u_n)
            base()
            n_u_n += 1
        elif opcion == 6 and n_u_l != muestras:
            data(N,Tipo,'U','L',n_u_l)
            base()
            n_u_l += 1
    valores,n_b,n_d_h,n_d_n,n_d_l,n_u_h,n_u_n,n_u_l=0
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N':
        break
    else:
        Run += 1


####
##############################################################################################################################################
###
#DataBase,DataHigh,DataNormal,DataLow= [], [], [], []

#operaciones = {'1': mainsiz, '2': mainiiz, '3': mainsde, '4': mainide}