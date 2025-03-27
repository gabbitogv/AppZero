import shutil,os

proyecto="PF-CE-093"
ext =".pdf"
origen ="C:\\app_py\\AppZero\\pdf\\"
destino = "C:\\app_py\\AppZero\\unir\\"
os.makedirs(origen,exist_ok=True)
os.makedirs(destino,exist_ok=True)

copia = []

cantidad = int(input("Cuantos archivos va a copiar:"))
cantidad +=1

for i in range(1,cantidad):
    v = 0
    app=""
    v = int(input("Ingrese pag. a copiar:"))
    
    if v < 10 :
        app = f"{proyecto}-0{str(v)}{ext}"        
    else:
        app = f"{proyecto}-{str(v)}{ext}"  
    
    copia.append(app) 

n=0
for archivo in copia:

    archivo_origen = os.path.join(origen, archivo)
    archivo_destino = os.path.join(destino, archivo)     

    if os.path.exists(archivo_origen):

        shutil.copy(archivo_origen,archivo_destino)
        print(f"{archivo}' copiado")
        n+=1

    else:

        print(f"{archivo} no se encuentra")

print(f"Total de {n} archivos copiados")