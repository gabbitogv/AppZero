import pandas as pd

def sumador1 (tapa,interior):
    soldadura = 10
    Esp_Pieza = 10
    tol = 1
    dist = 18
    cte1 = soldadura+2*(Esp_Pieza+tol)+dist

    return (2*tapa+interior+cte1)

def sumador2 (tapa,interior):
    Esp_Pieza = 10
    tol = 1       

    return (2*tapa+interior+2*tol+Esp_Pieza)

def int_l(y):

    ruta_archivo = r"C:\\app_py\\AppZero\\vini.xlsx"
    df = pd.read_excel(ruta_archivo, sheet_name="vini")
    
    print(df)
    val_1 = str(input("¿Cambiar datos Si (s) o No (n)?: "))
            
    if val_1 =="s":

        df.iloc[0, 0] = float(input("X1: "))
        df.iloc[0, 1] = float(input("Y1: "))
        df.iloc[2, 0] = float(input("X2: "))
        df.iloc[2, 1] = float(input("Y2: "))
        df.to_excel(ruta_archivo, sheet_name="vini", index=False)
        print("Actualizado")    

    x1 = df.iloc[0, 0]
    y1 = df.iloc[0, 1]    
    x2 = df.iloc[2, 0]
    y2 = df.iloc[2, 1]
    
    y = float(y)

    if (y1 - y2) == 0:
        return str("Indefinido")
    
    else:

        x = 0
        z1 = float(x1-x2)
        z2 = float(y1-y)
        z3 = float(y1-y2)
        z4 = (z2/z3)
        x = x1 -(z1*z4)        
        df.iloc[1, 0] = x
        df.iloc[1, 1] = y
        df.to_excel(ruta_archivo, sheet_name="vini", index=False)

        return x    

c_s = str(input("¿Vas a interpolar (i) o tomar medidas (m)?: "))

if str(c_s) == "i": 
    
    print("Interpolar: ")    
    y = input("Valor de y: ")
    print (int_l(y))

elif str(c_s) == "m":   
    
    print("Métrica: ")
    tapa = int(input("Espesor tapa (mm) :"))
    interior = int(input("interior (mm) :"))
    print (sumador1(tapa,interior))
    print (sumador2(tapa,interior))

else:
    print ("Fin del programa")