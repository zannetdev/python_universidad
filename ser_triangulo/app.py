from ast import If
from cmath import sqrt
import cmath
import math
import os
os.system('cls')
titulo = ""*10 + "VERICACIÓN DE RECTÁNGULO".title()
print(""*40 + titulo.upper())
lado_1 = float(input("Favor de ingresar el lado 1: "))
lado_2 = float(input("Favor de ingresar el lado 2: "))
lado_3 = float(input("Favor de ingresar el lado 3: "))
os.system("cls")
tipo_tr = ""
if lado_1 == lado_2 and lado_2 == lado_3 :
  tipo_tr = "EQUILÁTERO"
else:
  if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    tipo_tr = "ISÓCELES"
  else :
      if lado_1 != lado_2 and lado_2 != lado_3:
        tipo_tr = "ESCALENO"
print(str.format("DATOS DEL TRIÁNGULO: \n-LADO A: {} u\n-LADO B: {} u\n-LADO C: {} u\nTIPO DE TRIÁNGULO: {}", lado_1, lado_2, lado_3, tipo_tr))
input()

