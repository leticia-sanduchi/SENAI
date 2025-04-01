# -*- coding: UTF-8 -*-
print("Digite o seu peso e altura e direi se seu peso está favorável ou não")
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc=peso/(altura*altura)
if imc<20:
    print("Você está abaixo do peso")
elif imc >=20 and imc <25:
     print("Você está com o peso normal")
elif imc >=25 and imc <30:
     print("Você está com sobre peso")
elif imc >=30 and imc <40:
     print("Você está obeso")
else:
    imc >=40
    print("Você está com obesidade mórbida")
