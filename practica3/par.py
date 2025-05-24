#Numero par e impar

x= 5
while x<=5:
    try:
        numero = int(input("Introduce un número entero: "))
        if (numero<=0):
            raise ValueError("Debes ingresar un numero mayor a cero.")
        
        if(numero%2==0):
            print("El número ingresado es par.")
        else:
            print("El número ingresado es impar.")
    except (ValueError) as e:
        if str(e).startswith("Debes ingresar"):
            print("Error: ",e)
        else:
            print("Error: No se ingreso un numero entero")
    