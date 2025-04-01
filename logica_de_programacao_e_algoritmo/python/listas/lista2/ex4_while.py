print("Digite vários números inteiros e positivos e mostrarei a soma dos números pares e a soma dos números ímpares. O programa vai parar quando você digitar um número maior que 1000")

pares=0
impares=0

while True:
    num=int(input("Digite um valor: "))

    if num>1000:
        print(f"A soma dos números ímpares é de: {impares} e a soma dos números pares é de: {pares}")
        break
    
    elif num%2 == 0:
        pares = pares + num

    elif num%2 != 0:
        impares=impares+num
