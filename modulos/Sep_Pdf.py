import os
import fitz


def izquierda(palabra,n):
    return palabra[:n]

def sep_pdf(carpeta_in,archivo_out):    
    nt = 0
    na = 0

    for nombre_archivo in os.listdir(carpeta_in):
    
        if nombre_archivo.lower()[-4:] =='.pdf':

            na += 1       
            ruta_archivo = os.path.join(carpeta_in,nombre_archivo)            
            nombre_archivo_exp = izquierda(nombre_archivo,len(nombre_archivo)-4)            
            pdf = fitz.open(ruta_archivo)
            
            for pagina_num in range(pdf.page_count):
                
                pdf_salida = fitz.open()                
                pdf_salida.insert_pdf(pdf, from_page=pagina_num, to_page=pagina_num)                
                
                if pagina_num +1< 10 :                    
                    nombre_archivo = f"{archivo_out}{nombre_archivo_exp}-0{pagina_num + 1}.pdf"
                    
                else:
                    nombre_archivo = f"{archivo_out}{nombre_archivo_exp}-{pagina_num + 1}.pdf"

                    
                pdf_salida.save(nombre_archivo)
                pdf_salida.close()                

            nt+= pagina_num
    
    return print(f"Página {nt + na} cantidad de archivos {na}")