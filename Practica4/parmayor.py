'''
Escribir un programa que pida al usuario un número entero positivo mayor de 10 y
que muestre como resultado todos los números impares desde 2 hasta ese número
separados por comas.
'''

x= 5
while x<=5:
    try:
        limite = int(input("Introduce un número entero mayor a 10: "))
        if (limite<=10):
            raise ValueError("Debes ingresar un numero mayor a diez.")
        
        impares= [str(i) for i in range(2, limite+1) if i%2!=0]
        resultado = ", ".join(impares)

        print("Los numeros impares desde 2 hasta", limite, "son: ", resultado)

    except (ValueError) as e:
        if str(e).startswith("Debes ingresar"):
            print("Error: ",e)
        else:
            print("Error: No se ingreso un numero entero")
