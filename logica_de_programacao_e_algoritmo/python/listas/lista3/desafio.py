print("Contarei quantos dígitos tem o número que você digitar")
num = int(input("Digite o número: "))
contagem = 0
          
def cont(num):
    global contagem
    while num>=1:
        num = num/10
        contagem +=1

cont(num)
print(f"O número '{num}' tem {contagem} dígitos")
