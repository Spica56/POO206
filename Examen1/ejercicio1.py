#Letra más grande

x= 5
while x==5:
    try:
        p1 = input("Escribte una palabra:")

        p2 = input("Escribe otra palabra: ")

        if len(p1)== len(p2):
            raise ValueError("Las dos palabras tienen el mismo tamaño")

        if len(p1) > len(p2):
            x1 = len(p1)
            x2 = len(p2)
            x1 = x1-x2
            print("La palabra ", p1, " es más larga que ", p2, " por", x1, "letras")
        else:
            x1 = len(p2)
            x2 = len(p1)
            x1 = x1-x2
            print("La palabra ", p2, " es más larga que ", p1, " por", x1, "letras")

    except input as e:
        if str(e).startswith("Las dos"):
            print("Error: ", e)
        else:
            print("Error: No ingresaste un número")
    finally:
        print("Intenta escribir dos nuevas palabras. 👍")