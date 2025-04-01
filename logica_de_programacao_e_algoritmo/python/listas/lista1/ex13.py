# -*- coding: UTF-8 -*-
print("Diga suas três notas e o seu número de faltas e direi se você está aprovado, reprovado por falta ou reprovado por média")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
faltas=int(input("Digite o número de faltas: "))
media=(nota1+nota2+nota3)/3
if faltas>= 20:
    print("Você está reprovado por faltas")
elif media<7:
    print("Você está reprovado pela média")
else:
    print ("Você está aprovado")

