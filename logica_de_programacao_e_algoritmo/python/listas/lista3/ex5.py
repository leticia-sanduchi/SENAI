print("Direi se o número que você digitar é primo ou não. Digite um número maior que 1.")
num=int(input("Digite o número: "))

def primo(num):
        cont=0
        for i in range(1,num):
                if num%i==0:
                        cont+=1
        if cont == 1:
            print("O número é primo")
        else:
            print("O número não é primo")

primo(num)
