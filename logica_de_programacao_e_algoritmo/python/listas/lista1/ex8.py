# -*- coding: UTF-8 -*-
print("Diga seu salário e o valor da prestação e direi vou informar se é possível realizar o empréstimo ou não")
salario=float(input("Digite o valor do salário: "))
prestacao=int(input ("Digite o valor da prestação: "))
if prestacao>salario*0.3:
    print("O seu empréstimo não poderá ser realizado")
else:
    print("O seu empréstimo poderá ser realizado")
