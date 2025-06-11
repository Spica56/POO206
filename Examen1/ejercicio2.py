#Serie de Collatz

x= 5
while x==5:
    try:
        c = int(input("Introduce un número: "))

        print(c)
        while c>1:
            if c%2== 0:
                c= c/2
            else:
                c= c*3
            print(c, ", ")
        print("1")


    except input as e:
        print("Error: ", e)
    finally:
        print("El ejercicio estaba difícil. 👍")