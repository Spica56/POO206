"""try:
    numero = int(input("Introduce un número: "))
    resultado = 10/numero
    
    print("Resultado:", resultado) 

except ValueError:
        print("Error: Se ingreso algo que no es un numero entero,")
except ZeroDivisionError:
      print("Error: Estas intentando dividir entre 0")
"""
# Multiples excepciones en una linea
"""
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print("Error: Se ingreso algo que no es un número entero." if isinstance(e, ValueError) else "Error: Estas intentando dividir entre 0.")
"""
#Uso de finally
"""
try:
    numero = int(input("introduce un número: "))
    resultado = 10 /numero
except (ValueError, ZeroDivisionError) as e:
    print("Error: Se ingreso algo que no es un número entero." if isinstance(e, ValueError) else "Error: Estas intentando dividir entre 0.")
finally:
    print("Gracias por ejecutar el programa.")
"""
#Uso de raise

def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    print("Acceso permitido.")

try:
    verificar_edad(16)
except ValueError as e:
    print(f"Error: {e}")

