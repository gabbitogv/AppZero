import shutil,os
import pandas as pd

copiador = r"C:\\app_py\\AppZero\\cp.xlsx"
source = r"C:\\app_py\\AppZero\pdf\\"
destino = r"C:\\app_py\\AppZero\\dwg\\"

os.makedirs(source, exist_ok=True)
os.makedirs(destino, exist_ok=True)

df = pd.read_excel(copiador, sheet_name="cp")
copia =[]
copia = df["resultado"].tolist()

for archivo in copia:

    ruta_origen = os.path.join(source, archivo)
    ruta_destino = os.path.join(destino, archivo)

    if os.path.exists(ruta_origen):
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"Archivo {archivo} copiado con éxito")
    else:
        print(f"Advertencia: {archivo} no existe en la carpeta origen")