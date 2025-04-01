print("Digite 4 notas e mostrarei as notas e a média na tela")

notas = [0, 0, 0, 0]
soma = 0
cont = 0

while cont < 4:
    nota[x] = float(input("Digite a nota: " % x))
    soma = soma + nota[x]
    x = x + 1
x = 0
while x < 4:
    print("Digite a nota: " % (x, nota[x]))
    x = x + 1
print("A média é: %5.2f" % (soma/x))
