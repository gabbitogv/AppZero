import os

def derecha(palabra,n):
    return palabra[-n:]

def izquierda(palabra,n):
    return palabra[:n]

def rename_inv():      
    directorio ="C:\\app_py\\AppZero\\dwg"
    os.chdir(directorio)
    archivos = os.listdir(directorio)
    
    for archivo in archivos:
          
        if "0_Sheet_" in archivo:              
            nuevo_nombre0 = archivo.replace("0_Sheet_", "")
        else:
            nuevo_nombre0 = archivo

        ext = derecha(nuevo_nombre0,len(nuevo_nombre0)-nuevo_nombre0.rfind('.'))
        nuevo_nombre1=izquierda(nuevo_nombre0,nuevo_nombre0.rfind('.'))        
        CP1 = nuevo_nombre1.rfind('-')+1
        nuevo_nombre2 = izquierda(nuevo_nombre1,CP1)
        num0 = int(derecha(nuevo_nombre1,len(nuevo_nombre1)-CP1))
        
 
        if num0 < 10:
            nuevo_nombre = f"{nuevo_nombre2}0{num0}{ext}"
        else:
            nuevo_nombre = f"{nuevo_nombre2}{num0}{ext}"
        
        
        if archivo != nuevo_nombre:        
            os.rename(archivo, nuevo_nombre)
        
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")

    return print(f"Proceso Terminado") 
          

def rename_sec(PROYECTO,EXT,plus):

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
                nk = 0
                
                if plus == 0:
                    nk = n
                else: 
                    nk = n + plus-1               
                       
                if n + plus < 10:
                    rename = f"{PROYECTO}-0{str(nk)}.{EXT}"
                else:
                    rename = f"{PROYECTO}-{str(nk)}.{EXT}"
            
                os.rename(archivo, rename)
                print(f"{archivo} --> {rename}")
    else:
        print("PROYECTO no puede ser vacio")


#rename_sec("CT10 09042025 CS026 PDF","pdf",0)