print("Digite números e calcularei a soma e a média deles. Digite um número negativo para sair")
soma =0
contador=0
while True:
    num=float(input("Digite seus números: "))

    if num<0:
        break
    soma=soma+num
    contador=contador+1
    
print("A soma dos números é: ", num)
print("A média dos números é: ", num/contador)


    
