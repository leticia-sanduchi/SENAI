# -*- coding: UTF-8 -*-

velocidade=int(input("Digite a velocidade em km do carro: "))
if velocidade >80:
    valor_multa=(velocidade-80)*5
    km_acima=velocidade-80
    print(f"Você passou {km_acima} kilômetros acima da velocidade permitida, totalizando uma multa de R${valor_multa}")
elif velocidade <80:
    print(f"Você estava em uma velocidade de {velocidade}, o que é permitido na via, ou seja, sem multas")
else:
    print("Erro")
