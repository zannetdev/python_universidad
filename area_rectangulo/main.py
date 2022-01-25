from ast import If
from datetime import datetime
pi = 3.14159
inx = 1
import os
while inx > 0:
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    os.system('cls')
    print(str.format("GONZALEZ GONZALEZ EDUARDO \nPROGRAMACIÓN ORIENTADA A OBJETOS\nFECHA DE HOY: {} \n",fecha_hoy))
    strOptions = "1. ÁREA DE TRIÁNGULO \n2. ÁREA DE CIRCULO \n3. ÁREA DE RECTÁNGULO \n4. SALIR\n\n\n"
    print(str.format("{}", strOptions))
    op = int(input("Favor de ingresar una opción: "))
    if op == 1:
        ##CALCULAMOS
        base = float(input("\nIngrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        res = (base * altura) / 2
        print(str.format("El area del triángulo es: {}", res))
        input()
    if op == 2:
        radio = float(input("Ingrese el radio del circulo: "))
        res = ((pi * radio)**2)
        print(str.format("El area del circulo es: {}", res))
        input()
    if op == 3:
        base = float(input("\nIngrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        res = (base * altura)
        print(str.format("El area del rectángulo es: {}", res))
        input()
    if op == 4:
        inx = 0
        print("Saliendo...")
# num = 3
# if num > 0:
#     print(num, "is a positive number.")
# print("This is always printed.")

# num = -1
# if num > 0:
#     print(num, "is a positive number.")
# print("This is also always printed.")
