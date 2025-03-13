import os
import sys
from modulos.Sep_Pdf import sep_pdf
from modulos.Uni_pdf import unir_pdf
from modulos.rename_ar import izquierda, derecha

def switch_control(option):
#    if opcion==5:
#        eject = sep_pdf(carpeta_in,archivo_out)
#     elif opcion == 6:
#        unir_pdf(carpeta_in,archivo_out)
#    else:
#        eject = print("Sin programa")
#    return eject
     return print(opcion)
# Archivos útiles
carpeta_in = 'C:\\app_py\\AppZero\\Sep'
archivo_out = 'C:\app_py\\AppZero\\Pdf'



script_dir = os.path.dirname(os.path.abspath(__file__))
carpeta = os.path.join(script_dir, "modulos")

#sys.path.append(carpeta)

# Obtener los archivos .py en la carpeta "modulos"
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
        
        switch_control(opcion)  

    else:
        print("Selección inválida.")
    
except ValueError:
    print("Ingrese una opcion valida.")


