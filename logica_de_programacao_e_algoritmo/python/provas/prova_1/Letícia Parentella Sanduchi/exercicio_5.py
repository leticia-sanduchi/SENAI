print("Você vai digitar o valor de sua compra e eu aplicarei um desconto de 5% caso o valor seja entre R$50,00 e R$100,00. Mas caso a compra tenha um valor maior que R$100,00 o desconto aplicado será de 10%.")

valor_compra = float(input("Digite o valor da sua compra: "))

if valor_compra >=50 and valor_compra <=100:
    valor_desconto = valor_compra * 0.05
    valor_descontado = valor_compra - valor_desconto
    print(f"O valor de sua compra com um desconto de 5% aplicado é: R${valor_descontado}")

elif valor_compra >100:
    valor_desconto = valor_compra * 0.10
    valor_descontado = valor_compra - valor_desconto
    print(f"O valor de sua compra com um desconto de 10% aplicado é: R${valor_descontado}")

else:
    print(f"O valor de sua compra continua sendo R${valor_compra}")
