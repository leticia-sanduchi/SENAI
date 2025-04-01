print("Digite um número inteiro e eu direi o seu produto sem números negativos ou zero")

num = int(input("Digite o seu número: "))
acum = 1

def produto(num):
    global acum
    for i in range (num-1,0,-1):
        if num % i == 0:
            acum = acum*i
    if num == acum:
        print("Número perfeito")
    else:
        print("Não é um número perfeito")

produto(num)
