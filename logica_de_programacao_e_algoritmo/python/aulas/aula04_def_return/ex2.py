def multiplo (a,b):
    if a % b == 0:
        return True
    else:
        return False

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

resultado = multiplo(valor1,valor2)

if resultado:
    print("Os números são múltiplos")

else:
    print("Os números não são múltiplos")
