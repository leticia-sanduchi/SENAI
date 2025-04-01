print("Digite a altura e o raio de um cilindro e eu mostrarei o seu volume")

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

def volume(altura,raio):
    resultado = 3.14*(raio*raio)*altura
    print(f"O volume do cilindro é {resultado:.2f}")
volume(altura,raio)
