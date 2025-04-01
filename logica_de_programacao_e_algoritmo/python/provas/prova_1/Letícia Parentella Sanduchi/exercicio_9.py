print("Digite o valor dos lados dos triângulos e eu direi se ele é escaleno ou não.")

lado1=int(input("Digite um número inteiro: "))
lado2=int(input("Digite um número inteiro: "))
lado3=int(input("Digite um número inteiro: "))

if (lado1 != lado2) and (lado1 != lado3):
    print("É um triângulo escaleno")
        
elif (lado1+lado2<lado3) or (lado1+lado3<lado2) or (lado2+lado3<lado1):
    print("Não é um triângulo")

else:
    print("Não é um triângulo escaleno")

