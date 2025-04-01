print("Digite a idade de várias pessoas e mostrarei o total de pessoas com menos de 21 anos e o total de pessoas com mais de 50 anos. Digite -99 para sair.")

menos21=0
maior50=0

while True:
    idade=int(input("Digite as idades: "))
    if idade== -99:
        break
    if idade<21:
        menos21 = menos21 + 1
    elif idade>50:
        maior50 = maior50 + 1
print(f"O total de pessoas com idade menor que 21 é: {menos21}")
print(f"O total de pessoas com idade maior que 50 é: {maior50}")
