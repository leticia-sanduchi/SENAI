# -*- coding: UTF-8 -*-
print("Digite dois números e direi se o primeiro número é divisível pelo segundo número")
num1=int(input("Digite o primeiro valor: "))
num2=int(input ("Digite o segundo valor: "))
if num1 % num2 ==0:
    print(f"{num1} é divisível por {num2}")
else:
    print(f"{num1} não é divisível por {num2}")
