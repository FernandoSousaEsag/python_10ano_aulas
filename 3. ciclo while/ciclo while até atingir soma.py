
import os
os.system("cls")  # limpar o ecrã do terminal (funciona no Windows)
soma = 0
while soma < 20:
    numero = int(input("Introduza um número: "))
    soma = soma + numero

print(f"A soma atingiu {soma}.")