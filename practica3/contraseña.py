#Palindromo
import string

x= 5
while x<=5:
    try:
        c = input("Introduce una contraseña: ")
        if len(c) <10:
            raise ValueError("La contraseña es demasiado corta.")
        if all(char.isdigit() for char in c):
            raise ValueError("La contraseña debe contener al menos un número.")
        if all(char not in string.punctuation for char in c):
            raise ValueError("La contraseña debe contener al menos un carácter especial.")
        else:
            print("Contraseña Válida.")

    except (ValueError) as e:
        if str(e).startswith("La contraseña"):
            print("Error:",e)
        else:
            print("Error: contraseña invalida.")