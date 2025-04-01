print("Digite quantos números quiser e mostrarei o maior e o menor desses números. Digite um número negativo para sair.")
num=float(input("Digite os números: "))
menor= num
maior= num
while True:
    num=float(input("Digite os números: "))
    
    if num<0:
        break
    elif num>maior:
        maior=num
    elif num<menor:
        menor=num
print(f"O maior número digitado foi: {maior} e o menor número digitado foi {menor}")
