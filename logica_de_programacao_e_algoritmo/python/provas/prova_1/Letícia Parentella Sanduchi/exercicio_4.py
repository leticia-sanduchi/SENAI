print("Você irá digitar um número e eu mostrarei se ele é primo ou não. Digite um número maior que 1.")

num = int(input("Digite um número inteiro: "))
cont = 0

for i in range(1, num):
    if num % i == 0:
        cont = cont + 1
if cont == 1:
        print("O número é primo")

elif num == 1:
    print("Digite um número maior que 1")

else:
    print("O número não é primo")
