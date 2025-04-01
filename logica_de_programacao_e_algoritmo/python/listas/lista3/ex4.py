print("Farei uma contagem regressiva até zero")
num=int(input("Digite um número que você queira que inicie a sua contagem regressiva: "))


def contagem (num):
    for i in range(num,-1,-1):
        print(f"{i}")      

contagem(num)
print("Feliz ano novo!")   
