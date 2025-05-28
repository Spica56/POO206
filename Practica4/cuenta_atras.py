'''
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas
'''

x = 5

while x <=5 :
    try:
        numero = int(input("Introduce un numero entero positivo: "))
        
        if numero < 0:
            raise ValueError("Debes ingresar un número mayor a cero")
        Valor = ", ".join(str(i) for i in range(numero, -1,-1))
        print("La cuenta atras desde", numero, "hasta 0 es: ", Valor)
    
    except (ValueError) as e:
        if str(e).startswith("Debes ingresar"):
            print("Error: ",e)
        else:
            print("Error: No se ingreso un numero entero")