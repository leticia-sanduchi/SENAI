# -*- coding: UTF-8 -*-
import math

print("Escreva um número e direi a sua raiz quadrada caso ele seja positivo ou igual a 0, mas caso seja negativo direi o quadrado do número")
num=float(input("Digite número: "))
if num>=0:
    valor1=math.sqrt(num)
    print(f"O valor da raiz quadrada do número {num} é {valor1}")
elif num<0:
    valor1=pow(num, 2)
    print(f"O valor da potenciação do número {num} é {valor1}")
else:
    print("Erro")

