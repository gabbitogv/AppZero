import os

def derecha(palabra,n):
    return palabra[-n:]

def izquierda(palabra,n):
    return palabra[:n]

def rename_dwg(PROYECTO):      
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
              CP5 = derecha(archivo,len(archivo)-archivo.rfind("."))
              #print(f"CP1: {CP1} CP2: {CP2} CP3: {CP3} CP4: {CP4} CP5: {CP5}")

              #PROY = izquierda(CP3,CP4) mas adelante seleccionar que nombre usar, de un proyecto o el inyectado.
              
              NUM1 =int(derecha(CP3,len(CP3)-CP4-1))
          
              if NUM1 < 10:
                 NUM2 = "-0"+str(NUM1)
              else:
                 NUM2 ="-"+str(NUM1)       

              nuevo_nombre = f"{CP1}{PROYECTO}{NUM2}{CP5}"              
              os.rename(archivo, nuevo_nombre)
              print(f"Renombrado: {archivo} -> {nuevo_nombre}")

        else:

              print("Sin cambios")          

def rename_sec(PROYECTO,EXT):

    directorio ="C:\\app_py\\AppZero\\dwg"
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]    
    archivos = sorted(archivos)    
    n=0
    
    if len(PROYECTO)>0:
        
        for archivo in archivos:
        
                rename = ""        
                n+=1               
                       
                if n < 10:
                    rename = f"{PROYECTO}0{str(n)}.{EXT}"
                else:
                    rename = f"{PROYECTO}{str(n)}.{EXT}"
            
                os.rename(archivo, rename)
                print(f"{archivo} --> {rename}")
    else:
        print("PROYECTO no puede ser vacio")



#rename_sec(PROYECTO="PGENA700LL",EXT="dwg")