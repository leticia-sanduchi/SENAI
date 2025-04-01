#-*- coding: UTF-8 -*-
print("Digite um número e mostrarei os divisores desse número")
valor = int(input("Digite um número: "))

for i in range (1, valor, +1):
    if valor % i == 0:
          print(i)
          
