print("Vamos converter uma temperatura de Celsius para Fahrenheit e vice-versa")

temperatura = float(input("Digite a temperatura que você deseja converter: "))
conversao = input("Digite 'C' para converter de Clesius para Fahrenheit, e 'F' para converter de Fahrenheit para Celsius: ")
def cont_celsius(temperatura,conversao):
    if conversao == "C" or "c":
        cont_celsius = (temperatura - 32) * 5/9
        print(f"A temperatura em Celsius é: {cont_celsius: .2f}°C")

    elif conversao == "F" or "f":
        cont_fahrenheit = 9/5 * temperatura+32
        print(f"A temperatura em Fahrenheit é: {cont_fahrenheit: .2f}°F")

cont_celsius(temperatura,conversao)
