# -*- coding: UTF-8 -*-
print("Digite o número de horas trabalhadas e direi o valor do seu salário líquido")
horas=int(input("Digite o número de horas trabalhadas: "))
salario=horas*19.50
if salario>1500:
    impostorenda=salario*0.10
    salarioliquido=salario-impostorenda
    print(f"Com o desconto de R$ {impostorenda}, o valor líquido de seu salário é {salarioliquido}")
else:
    print(f"Seu salário líquido é {salario}")
              
