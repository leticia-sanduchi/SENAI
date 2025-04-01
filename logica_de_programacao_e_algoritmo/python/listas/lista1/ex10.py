# -*- coding: UTF-8 -*-
print("Diga três valores reais e informarei se eles podem ou não formar os lados de um triângulo e qual será o tipo do triângulo: equilátero, isósceles ou escaleno")
lado1=float(input("Digite um número: "))
lado2=float(input("Digite um número: "))
lado3=float(input("Digite um número: "))
if (lado1+lado2<lado3) or (lado1+lado3<lado2) or (lado2+lado3<lado1):
        print("Não é um triângulo")

elif (lado1==lado2) and (lado1==lado3):
    print("É um triângulo equilátero")

elif (lado1==lado2) or (lado1==lado3) or (lado2==lado3):
    print("É um triângulo isósceles")

else:
    print("É um triângulo escaleno")
