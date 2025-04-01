print("Digite valores e no final direi quantos valores entre 100 e 200 foram digitados. Digite 0 para sair")
cont = 0

while True:
    num = float (input("Digite os valores: "))
    
    if num >=100 and num <= 200:
        cont = cont + 1

    elif num == 0:
        print("Os valores digitados entre 100 e 200 é de: ", cont)
        break
