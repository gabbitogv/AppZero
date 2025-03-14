import os,sys,fitz

from modulos.rename_ar import izquierda,rename_sec
from modulos.sep_pdf import sep_pdf
#from modulos.uni_pdf import unir_pdf


def switch_control(asop):
    print(asop)
    if asop=="sep_pdf":
        eject = sep_pdf(carpeta_in,archivo_out)

    elif asop == "rename_ar":
        PROYECTO = str(input("Ingrese nombre proyecto: "))        
        eject = rename_sec(PROYECTO)

    else:
        eject = print("Sin programa")

    return eject    


# Archivos útiles
carpeta_in = 'C:\\app_py\\AppZero\\sep\\'
archivo_out = 'C:\\app_py\\AppZero\\pdf\\'
script_dir = os.path.dirname(os.path.abspath(__file__))
carpeta = os.path.join(script_dir, "modulos")

# Obtener los documentos .py de la carpeta modulos
archivos = [f for f in os.listdir(carpeta) if f.endswith(".py")]

if not archivos:
    print("No hay archivos .py disponibles.")
    exit()


print("Seleccione un archivo para ejecutar:")
for i, archivo in enumerate(archivos, 1):
        if not archivo=="__ini__.py":   
            print(f"{i}. {izquierda(archivo,len(archivo)-3)}")

try:
    opcion = int(input("Ingrese el número del archivo: "))
       
    if 1 <= opcion <= len(archivos):

        archivo_seleccionado = archivos[opcion - 1]
        ruta_completa = os.path.join(carpeta, archivo_seleccionado)

        print(f"Ejecutando {archivo_seleccionado}...\n")
        asop = izquierda(archivo_seleccionado,len(archivo_seleccionado)-3)
        switch_control(asop)  

    else:
        print("Selección inválida.")
    
except ValueError:
        print("Ingrese una opcion valida.")