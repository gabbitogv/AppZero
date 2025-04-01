import pandas as pd

def int_l(x1):

    ruta_archivo = r"C:\\app_py\\AppZero\\data.xlsx"    
    df = pd.read_excel(ruta_archivo, sheet_name="vini", dtype=float)    
    print(df)

    val_1 = str(input("¿Usar datos actuales Si (s) o No (n)?: "))
            
    if val_1 =="n":

        df.iloc[0, 0] = float(input("X0: "))
        df.iloc[0, 1] = float(input("Y0: "))
        df.iloc[2, 0] = float(input("X2: "))
        df.iloc[2, 1] = float(input("Y2: "))
        df.iloc[1,0] = float(x1)
        df.iloc[1,1] = 0      
    
    
    x0 = df.iloc[0, 0]
    y0 = df.iloc[0, 1]    
    x2 = df.iloc[2, 0]
    y2 = df.iloc[2, 1]
    x1 = float(x1)
    
    if (x0 - x2) == 0:
        return str("Indefinido")
    
    else:

        y1 = 0
        z0 = float(x0-x1)
        z1 = float(y0-y2)
        z2 = float(x0-x2)
        z3 = (z0*z1)/z2
        y1 = y0-z3        
        df.iloc[1, 0] = x1
        df.iloc[1, 1] = y1
        df.to_excel(ruta_archivo, sheet_name="vini", index=False)

    return print(df)