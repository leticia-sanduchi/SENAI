cont = 0
acum = 0

while True:
    valor = float (input("Digite valores e no final darei a média. Digite um valor negativo para sair: "))
    if valor < 0:
        print("você escolheu sair!")
        break
    acum = acum + valor
    cont = cont + 1
    media = acum / cont

print("A média dos valores digitados é de: ", media)
