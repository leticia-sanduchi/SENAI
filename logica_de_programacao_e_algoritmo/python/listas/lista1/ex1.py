# -*- coding: UTF-8 -*-

print("Farei a soma de dois valores, mas caso o valor somado seja maior que 20, vou somá-lo 8 ou caso o valor somado seja menor ou igual a 20, vou subtraí-lo 5")

num1=int(input("Digite o primeiro valor: "))
num2=int(input ("Digite o segundo valor: "))
soma=num1+num2
if soma>20:
    soma= num1+num2+8
    print("A sua soma é: ", soma)
elif soma<=20:
    soma=num1+num2-5
    print("A sua soma é: ", soma)
