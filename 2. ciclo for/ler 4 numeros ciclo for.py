import os
os.system("cls")  # limpar o ecrã

# Ler 4 números e calcular a média
soma=0
for i in range(1,5):
    numero = int(input(f"Introduza o {i}º número: "))   
    soma+=numero

media = soma / 4
print(media)