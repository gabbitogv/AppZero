import os

def derecha(palabra,n):
    return palabra[-n:]

def izquierda(palabra,n):
    return palabra[:n]


directorio ="C:\\Users\\Goren_Ingenieria\\Downloads\\Tratamiento\\dwg"

os.chdir(directorio)

archivos = os.listdir(directorio)

for archivo in archivos:
    
    if "0_Sheet_" in archivo:
        
        nuevo_nombre1 = archivo.replace("0_Sheet_", "")        

        CP1 = izquierda(nuevo_nombre1,3) #Tipo de Plano
         
        CP2 = derecha(nuevo_nombre1,len(nuevo_nombre1)-3)
        CP3 =izquierda(CP2,len(CP2)-4)        
        CP4 = CP3.find("-")

        PROYECTO = izquierda(CP3,CP4)
        NUM1 =int(derecha(CP3,len(CP3)-CP4-1))

        if NUM1 < 10:
            NUM2 = "-0"+str(NUM1)
        else:
            NUM2 ="-"+str(NUM1)       

        nuevo_nombre = CP1+PROYECTO+NUM2+".dwg"
        os.rename(archivo, nuevo_nombre)
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")

    else:

        print(f"Sin Cambios: {archivo}")