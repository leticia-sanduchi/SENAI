print("Digite um número de 1 a 10 e eu mostrarei a tabuada desse número")
num = int(input("Digite o número que você quer a tabuada: "))
          
def tabuada(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

tabuada(num)
          
