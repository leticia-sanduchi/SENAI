print("Digite o valor de uma mercadoria e o seu percentual de desconto e vou exibir o valor do desconto e o preço a pagar")
produto=float(input("Digite o valor do produto: "))
desconto=float(input("Digite a porcentagem de desconto: "))
valor_desconto=produto*desconto/100
valor_novo=produto-valor_desconto
print(f"O valor do desconto é: {valor_desconto} e o preço novo a se pagar é: {valor_novo}")
