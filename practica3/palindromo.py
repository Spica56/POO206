#Palindromo

x= 5
while x<=5:
    try:
        c = input("Introduce una palabra: ").lower()
        if  not c.strip():
            raise ValueError("No ingresaste nada.")
        if any(char.isdigit() for char in c):
            raise ValueError("No se permiten numeros.")
        if len(c)==1:
            raise ValueError()

        if c == c[::-1]:
            print("Es un palindromo.")
        else:
            print("No es un palindromo.")
    except (ValueError) as e:
        if str(e).startswith("No "):
            print("Error: ",e)
        else:
            print("Error: no se ingreso una palabra.")