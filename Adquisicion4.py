# import necessary packages
import cv2
import serial.tools.list_ports
import pandas as pd
import random
import os

# define necessary folders
Folderbydata = "Recoleccion2" # Folder de guardado de los archivos      S#(R/L)(D/U)(H/N/L)_R#M#.CSV
Folderbyimage = "TareasImagenes" # Folder donde estan las imagenes          (R/L)(D/U)(H/N/L).jpg

# define variables
Data = []
n_b = 0
n_d_h , n_d_n , n_d_l = 0 , 0 , 0
n_u_h , n_u_n , n_u_l = 0 , 0 , 0
valores = 0
Id_display = 'Tareas_Motrices-Adquisicion_de_datos'
opciones = ["Base","Down High","Down Normal","Down Low","Up High","Up Normal","Up Low"]
opcionesR = ["B","RDH","RDN","RDL","RUH","RUN","RUL"]
opcionesL = ["B","LDH","LDN","LDL","LUH","LUN","LUL"]

# lee las imagenes y selecciona una de forma aleatoria
def readfolderimage(Tipo): 
    # Get the list of files in the folder
    files=os.listdir(Folderbyimage)
    # Randomly select a file from the list
    while True:
        file = random.choice(files)
        # verifica el resultado es nul o no
        if file == None:
            pass
        else:
            if len(file.split('.')[0]) == 1 :
                return file
            elif (file.split('.')[0].startswith(Tipo)):
                return file
            
    
# lee los .csv y verifica si el sujeto ya existe y devuelve cuantas muestras tenemos de ese sujeto
def readfolderdata(Subjet,Tipo):
    # Get the list of files in the folder
    try :
        files=os.listdir(Folderbydata)
    except:
        # si no existe el folder se crea
        os.mkdir(Folderbydata)
    files=os.listdir(Folderbydata)
    # lee el archivo de la carpeta y verifica si el sujeto ya existe
    count = 0
    for x in range(0,len(files)):
        if files[x].split('.')[0].split('_')[1].startswith('B'):
            pass
        elif files[x].split('.')[0].split('_')[1].startswith(Tipo) and files[x].split('.')[0].split('_')[0].split('S')[1] == Subjet:
            count = count + 1
    return count/6

# imagen base para encuadre
def base():
    cv2.namedWindow(Id_display, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(Id_display, 1350,750)
    cv2.imshow(Id_display, cv2.imread(Folderbyimage+'/B.jpg'))
    cv2.waitKey(250)
#base()

# Show the available ports
ports = serial.tools.list_ports.comports()
portList=[]
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

# Select the port
val = input("select port COM:")
for x in range(0,len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar = "COM"+str(val)
        print(portList[x])

# configure the serial port
serialInst = serial.Serial()
serialInst.baudrate = 115200
serialInst.port = portVar


#(R/L)(D/U)(H/N/L).jpg
#S#_(R/L)(D/U)(H/N/L)_M#.CSV
def dataacquisition(Subject,Tarea,Muestra):
    cv2.imshow(Id_display, cv2.imread(Folderbyimage+'/'+Tarea))
    cv2.waitKey(500)
    serialInst.open()
    while True:
        packet = serialInst.readline()
        try:
            d = int(packet.strip().decode('utf-8'))
        except (ValueError, TypeError):
            pass
        else:
            Data.append(d)
        if len(Data) == 500:# Numero de datos a 100Hz
            pd.DataFrame(Data).to_csv(Folderbydata+'/'+"S"+str(Subject)+'_'+str(Tarea.split('.')[0])+'_'+"_M"+str(int(Muestra))+".CSV", index=False, header=False)
            Data.clear()
            #senal de off
            serialInst.close()
            cv2.imshow(Id_display, cv2.imread(Folderbyimage+'/B.jpg'))
            cv2.waitKey(2000)
            break


Subject = input('Ingresar identificación del sujeto: ')                     # Subject
Muestras = int(input('Ingresar numero de muestras : '))                     # Muestras
Tipo = input('Ingresar el tipo de experimento a realizar (L/R): ').upper()  # Tipos posibles L , R

while __name__ == '__main__':
    base()
    passkey = input('Todos listos (K):').upper()
    while passkey != 'K':
        pass 
    
    muestrasprevias = readfolderdata(Subject,Tipo)
    n_b = muestrasprevias
    n_d_h , n_d_n , n_d_l = muestrasprevias , muestrasprevias , muestrasprevias
    n_u_h , n_u_n , n_u_l = muestrasprevias , muestrasprevias , muestrasprevias
    Muestras = muestrasprevias + Muestras

    while valores != (7*Muestras):# Numero de variables * Numero de muestras
        
        imagen = readfolderimage(Tipo)
        print(imagen)
        if Tipo == 'L':
            opcion = opcionesL.index(imagen.split('.')[0])
        else:
            opcion = opcionesR.index(imagen.split('.')[0])
        print("aleatorio :"+ str(opcion) +" "+opciones[opcion])

        if opcion == 0 and n_b != Muestras:
            dataacquisition(Subject,imagen,n_b)
            n_b += 1
        elif opcion == 1 and n_d_h != Muestras:
            dataacquisition(Subject,imagen,n_d_h)
            n_d_h += 1
        elif opcion == 2 and n_d_n != Muestras:
            dataacquisition(Subject,imagen,n_d_n)
            n_d_n += 1
        elif opcion == 3 and n_d_l != Muestras:
            dataacquisition(Subject,imagen,n_d_l)
            n_d_l += 1
        elif opcion == 4 and n_u_h != Muestras:
            dataacquisition(Subject,imagen,n_u_h)
            n_u_h += 1
        elif opcion == 5 and n_u_n != Muestras:
            dataacquisition(Subject,imagen,n_u_n)
            n_u_n += 1
        elif opcion == 6 and n_u_l != Muestras:
            dataacquisition(Subject,imagen,n_u_l)
            n_u_l += 1
        else:
            pass
        valores = n_b + n_d_h + n_d_n + n_d_l + n_u_h + n_u_n + n_u_l
    
    cv2.destroyAllWindows()
    n_b = 0
    n_d_h , n_d_n , n_d_l = 0 , 0 , 0
    n_u_h , n_u_n , n_u_l = 0 , 0 , 0
    valores = 0
    Data.clear()
    
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N' or continuar == 'n':
        print("Fin de la recolección")
        break
    else:
        pass


