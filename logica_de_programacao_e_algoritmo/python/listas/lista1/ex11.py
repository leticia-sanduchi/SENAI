# -*- coding: UTF-8 -*-
print("Digite duas notas e direi se você está aprovado, reprovado ou de recuperação")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2

if media>=7:
    print("Você está aprovado")
elif media<3:
    print("Você está reprovado")
else:
    print("Você está de recuperação")

