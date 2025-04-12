import pandas as pd
import os

def derecha(palabra,n):
    return palabra[-n:]

def izquierda(palabra,n):
    return palabra[:n]

def guardar_simple(ruta, df1, df2):
    try:
        # Eliminar archivo si existe
        if os.path.exists(ruta):
            os.remove(ruta)
            
        # Crear nuevo archivo con los datos
        with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
            df1.to_excel(writer, sheet_name='data1', index=False)
            df2.to_excel(writer, sheet_name='data2', index=False)
        
        print("Datos guardados exitosamente")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
ini = input('prefijo: ')
len(ini)
ruta_archivo = r"C:\\pt\\data ini.xlsx"
ruta_archivo_out = r"C:\\pt\\data out.xlsx"    
df = pd.read_excel(ruta_archivo, sheet_name="data")
df2 = df[df['ORIGEN'] != 'ACCESORIO']
df2['INICIO'] = df2['PIEZA'].str.startswith(ini).map({True: 'Si', False: 'No'})
df2 = df2[df2['INICIO'] == 'Si']
df2 = df2.drop('INICIO', axis = 1)
df2['INICIO'] = df2['PIEZA'].str.len()-len(ini)
df2['INICIO2'] = df2.apply(lambda row: derecha(row['PIEZA'], n=row['INICIO']), axis=1)
df2['INICIO3'] = pd.to_numeric(df2['INICIO2'], errors='coerce')
print(df2)



maxnum = df2['INICIO3'].max()

df_nuevo = pd.DataFrame({
    'id': range(1, maxnum + 1)  # Crear secuencia desde 1 hasta maxnum
})

df_nuevo['Estado'] = df_nuevo['id'].isin(df2['INICIO3']).map({
    True: 'Encontrado',
    False: 'No encontrado'
})

guardar_simple(ruta_archivo_out,df2,df_nuevo)

print("terminado")

