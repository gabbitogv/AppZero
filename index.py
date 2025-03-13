import os
import sys
from modulos.Sep_Pdf import sep_pdf
from modulos.rename_ar import izquierda, derecha

def switch_control(option):
    if opcion==5:
        eject = sep_pdf(carpeta_in,archivo_out)
    else:
        eject = print("Sin programa")
    return eject

# Archivos útiles
carpeta_in = 'C:\\Users\\Goren_Ingenieria\\Downloads\\Tratamiento\\Sep'
archivo_out = 'C:\\Users\\Goren_Ingenieria\\Downloads\\Tratamiento\\Pdf\\'

# Obtener la ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la carpeta "modulos" al sys.path usando la ruta absoluta
carpeta = os.path.join(script_dir, "modulos")
sys.path.append(carpeta)

# Obtener los archivos .py en la carpeta "modulos"
archivos = [f for f in os.listdir(carpeta) if f.endswith(".py")]

if not archivos:
    print("No hay archivos .py disponibles.")
    exit()

print("Seleccione un archivo para ejecutar:")
for i, archivo in enumerate(archivos, 1):
    if not archivo=="__ini__.py":
        print(f"{i}. {archivo}")

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
    print("Ingrese un número válido.")


