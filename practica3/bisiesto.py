#Año bisiesto

x= 5
while x<=5:
    try:
        a = int(input("Introduce un año: "))
        if (a<=0):
            raise ValueError("Debes ingresar un año mayor a cero.")
        if(a%4==0):
            if(a%100==0 and a%400 !=0):
                print("No es un año bisiesto")
            else:
                print("Es un año bisiesto.")
        else:
            print("No es un año bisiesto.")
    except (ValueError) as e:
        if str(e).startswith("Debes ingresar"):
            print("Error: ",e)
        else:
            print("Error: No se ingreso un numero entero")
    finally:
        print("Los años bisiestos tienen 366 días y se añaden en febrero.")