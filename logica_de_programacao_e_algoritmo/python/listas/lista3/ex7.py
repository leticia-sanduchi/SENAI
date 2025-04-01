print("Faremos um cálculo com um dos quatro operadores matemáticos simples(adição, subtração, multiplicação ou divisão) com dois números")

num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operador = input("Digite um operador matemático simples com os símbolos: '+' para adição; '-' para subtração; '*' para multiplicação; '/' para divisão: ")

def soma(num, operador, num2):
        return num + num2
    
def subtracao(num, operador, num2):
        return num - num2

def multiplicacao(num, operador, num2):
        return num * num2

def divisao(num, operador, num2):
        return num /num2
    
if operador == "+":
    print(soma(num, operador, num2))
    
elif operador == "-":
    print(subtracao(num, operador, num2))

elif operador == "*":
    print(multiplicacao(num, operador, num2))

elif operador == "/":
    print(divisao(num, operador, num2))
