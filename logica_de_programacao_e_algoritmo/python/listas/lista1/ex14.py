# -*- coding: UTF-8 -*-
print("Diga o valor do produto e mostrarei o valor para a sua venda")
valor_produto=float(input("Digite o valor do produto: "))
if valor_produto<20:
   aumento=valor_produto*0.45
   lucro=valor_produto+aumento
   print(f"O seu produto comprado por {valor_produto} terá um valor de venda de {lucro}")
elif valor_produto>20:
    aumento=valor_produto*0.30
    lucro=valor_produto+aumento
    print(f"O seu produto comprado por {valor_produto} terá um valor de venda de {lucro}")
