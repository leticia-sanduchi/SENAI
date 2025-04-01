#-*- coding: UTF-8 -*-

print("Digite um número e apresentarei o fatorial desse número")
num = int(input("Digite um número para apresentar o seu fatorial: "))
fatorial = 1

for i in range (1, num+1, 1):
    fatorial = i * fatorial
print ("o resultado da fatorial é: ", fatorial)
