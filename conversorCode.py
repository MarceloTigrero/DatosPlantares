from locale import normalize
import os
import numpy as np
import pandas as pd


##############################################################################################################################
# Conversion de codificacion 
#   S#(R/L)(U/D)(H/N/L)_R#M#.csv -> S#_(R/L)(U/D)(H/N/L)_M#.csv
##############################################################################################################################


Folderbydata = 'Recoleccion1'   
Folderbydatanew = Folderbydata+'_Conversion'

Sujetos ={}
try:
    os.mkdir(Folderbydatanew)
except:
    pass

files = os.listdir( Folderbydata )



for file in files:
    name = file.split('.')[0]
    text = name.split("_")[0]
    rep = int(name.split("_")[1].split("M")[1])

    S = ''
    for x in range(0,len(text)):
        try:
            int(text[x])
        except:
            pass
        else:
            S += text[x]
    tarea = text[len(S)+1:]

    if S not in Sujetos:
        Sujetos[S] = {}
        Sujetos[S][tarea] = []
        Sujetos[S][tarea].append(rep)
        # copy file to new folder
        os.system('cp '+Folderbydata+'/'+file+' '+ Folderbydatanew+'/S'+S+'_'+tarea+'_M'+str(rep)+'.csv')
    else:
        if tarea not in Sujetos[S]:
            Sujetos[S][tarea] = []
            Sujetos[S][tarea].append(rep)
            # copy file to new folder
            os.system('cp '+Folderbydata+'/'+file+' '+ Folderbydatanew+'/S'+S+'_'+tarea+'_M'+str(rep)+'.csv')
        else:
            if rep not in Sujetos[S][tarea]:
                Sujetos[S][tarea].append(rep)
                # copy file to new folder
                os.system('cp '+Folderbydata+'/'+file+' '+ Folderbydatanew+'/S'+S+'_'+tarea+'_M'+str(rep)+'.csv')
            else:
                # cual es el repeticion mas grande?
                Sujetos[S][tarea].append(max(Sujetos[S][tarea])+1)
                # copy file to new folder
                os.system('cp '+Folderbydata+'/'+file+' '+ Folderbydatanew+'/S'+S+'_'+tarea+'_M'+str(max(Sujetos[S][tarea])+1)+'.csv')
# ordena los repeticiones de cada sujeto

#for S in Sujetos:
#    for tarea in Sujetos[S]:
#        Sujetos[S][tarea].sort()

#print(Sujetos)