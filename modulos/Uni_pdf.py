import os
import fitz

def unir_pdf(carpeta_in,archivo_out):

    pdf_salida = fitz.open()
    
    n = 0

    for nombre_archivo in os.listdir(carpeta_in):

        n += 1   

        if nombre_archivo.lower()[-4:] =='.pdf':           

            print(nombre_archivo)
            ruta_archivo = os.path.join(carpeta_in,nombre_archivo)

            pdf = fitz.open(ruta_archivo)

            pdf_salida.insert_pdf(pdf)

            pdf.close()
        
        else:
            n+=-1
    
    pdf_salida.save(archivo_out)

    pdf_salida.close()

    return print(f"{n} archivos unidos correctos")


carpeta_in='C:\\app_py\\AppZero\\Unir'



