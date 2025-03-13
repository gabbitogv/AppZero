import os

def derecha(palabra,n):
    return palabra[-n:]

def izquierda(palabra,n):
    return palabra[:n]

def rename_dwg():

    directorio ="C:\\app_py\\AppZero\\dwg"
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

            print("Sin cambios")          

def rename_sec(PROYECTO):

    directorio ="C:\\app_py\\AppZero\\dwg"
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]
    archivos = sorted(archivos)
    n=0
    
    for archivo in archivos:
        
            rename = ""        
            n+=1               
            
            if n < 10:
                rename = f"{PROYECTO}0{str(n)}.pdf"
            else:
                rename = f"{PROYECTO}{str(n)}.pdf"
            
            os.rename(archivo, rename)
            print(f"{archivo} --> {rename}")
        
        

     
    
PROYECTO = str(input("Ingrese nombre proyecto: "))
print(PROYECTO)
rename_sec(PROYECTO)