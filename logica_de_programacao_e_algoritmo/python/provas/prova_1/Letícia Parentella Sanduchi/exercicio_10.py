print("Digite o valor inicial, a taxa de juros e o número de períodos, e mostrarei o valor final com juros compostos")

valor_inicial = float(input("Digite o valor inicial: "))
taxa_juros = float(input("Digite a txa de juros: "))
periodos = float(input("Digite o número de períodos: "))

resultado = valor_inicial*(1+taxa_juros)*periodos
print("O valor final com juros compostos é: ",resultado)
