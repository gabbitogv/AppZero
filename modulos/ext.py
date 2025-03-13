import zipfile
import os

def comp(directorio):

    if directorio is not None:

        for archivo in os.listdir(directorio):

            if archivo.endswith(".zip"):
                ruta_completa = os.path.join(directorio, archivo)

                with zipfile.ZipFile(ruta_completa, 'r') as zip_ref:
                    zip_ref.extractall(directorio)
                    print(f"Archivo descomprimido: {archivo}")



