import os
import fitz

def unir_pdf(carpeta_in,archivo_out,PROYECTO):

    pdf_salida = fitz.open()
    n = 0

    for nombre_archivo in os.listdir(carpeta_in):

        n += 1

        
        if nombre_archivo.lower()[-4:] =='.pdf':           

                ruta_archivo = os.path.join(carpeta_in,nombre_archivo)
                pdf = fitz.open(ruta_archivo)
                pdf_salida.insert_pdf(pdf)
                pdf.close()
        
        else:
                n+=-1
    

    if len(PROYECTO)>0:    
        pdf_out=f"{archivo_out}{PROYECTO}.pdf"
        pdf_salida.save(pdf_out)
        pdf_salida.close()
        return print(f"{n} archivos unidos correctos")
    
    else:
        pdf_salida.close()
        return print("PROYECTO no puede ser vacio")