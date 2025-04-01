# -*- coding: UTF-8 -*-
print("Diga a temperatura atual e direi como está o clima hoje")
temperatura=int(input("Digite a temperatura atual: "))
if temperatura<=15:
    print("Está muito frio")
elif temperatura >=16 and temperatura <=23:
    print("Está frio")
elif temperatura >23 and temperatura <=26:
    print("Está agradável")
elif temperatura >26 and temperatura <=31:
    print("Está calor")
elif temperatura >31:
    print("Está muito quente")
    
