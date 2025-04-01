s = 0
while True:
    num = int(input("Digite números e mostrarei o triplo de cada um. Digite -999 para sair: "))

    if num != -999:
        valor=num*3
        print(f" O valor é: {valor}")

    else:
        print("Saindo...")
        break
