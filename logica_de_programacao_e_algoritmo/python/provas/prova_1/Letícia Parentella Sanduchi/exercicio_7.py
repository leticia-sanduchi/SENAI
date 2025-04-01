print("Digite o valor dos lados dos triângulos e eu direi se ele é equilátero ou não.")

lado1=float(input("Digite um número: "))
lado2=float(input("Digite um número: "))
lado3=float(input("Digite um número: "))

def equilatero(lado1,lado2,lado3):
    if (lado1==lado2) and (lado1==lado3):
        print("É um triângulo equilátero")
        
    elif (lado1+lado2<lado3) or (lado1+lado3<lado2) or (lado2+lado3<lado1):
        print("Não é um triângulo")

    else:
        print("Não é um triângulo equilátero")

equilatero(lado1,lado2,lado3)
