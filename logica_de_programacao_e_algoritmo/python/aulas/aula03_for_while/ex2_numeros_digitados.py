print("Digite números positivos e mostrarei quantos números foram digitados. Digite um número negativo para sair")
x = 0
while True:
    valor1 = float(input("Digite os números: "))
    if valor1 <= 0:
        print("Você saiu")
        break
    if valor1 > 0:
        x = x + 1
print("o valor da contagem é de: ", x)
        
