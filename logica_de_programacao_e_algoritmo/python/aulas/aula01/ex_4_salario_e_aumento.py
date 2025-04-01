print("Irei calcular o aumento e o valor do novo salário")
salario=float(input("Digite o valor do salário: "))
porcentagem=float(input("Digite a porcentagem de aumento"))
aumento=salario*porcentagem/100
salario_novo=salario+aumento
print(f"O aumento foi de: {aumento} e o salário novo ficou: {salario_novo}")
