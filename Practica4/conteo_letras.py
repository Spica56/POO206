'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

x = 5

while x <= 5:
    try:
        frase = input("Introduce una frase: ").lower()
        
        if any(char.isdigit() for char in frase):
            raise ValueError("Debes ingresar una frase, no un número.")
        if  not frase.strip():
            raise ValueError("No ingresaste nada.")
            
        letra = input("Introduce una letra: ")

        if any(char.isdigit() for char in letra):
            raise ValueError("Debes ingresar una letra, no un número.")
        if len(letra) != 1:
            raise ValueError("Debes ingresar una sola letra.")
        
        cantidad = frase.count(letra)
        print("La letra", letra, "aparece ", cantidad, " en la frase.")
    except (ValueError) as e:
        print("Error: ", e)